def is_overlapping(subtitle, window) -> bool :
    return(
        subtitle["start"] < window["end"] and subtitle["end"] > window["start"]
    )

def map_windows_to_subtitles(windows, subtitles, audio_id : str, audio_path : str):
    dataset = []
    for window in windows:
        matching_subtitles = []

        for subtitle in subtitles:
            if is_overlapping(subtitle, window):
                relative_start = max(subtitle["start"], window['start']) - window["start"]
                relative_end = min(subtitle["end"],window["end"]) - window["start"]
                matching_subtitles.append({"start": relative_start, "end": relative_end, "text":subtitle["text"],"layer":subtitle["layer"]})
        dataset.append({
            "audio_id" : audio_id,
            "audio_path" : audio_path,
            "window":{"start" : window["start"], "end" : window["end"]},
            "subtitles": matching_subtitles
        })
    return dataset