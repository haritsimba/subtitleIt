import json
from src.preprocessing.dataset import map_windows_to_subtitles
from src.preprocessing.subtitles import load_sub_csv_to_dict
from src.preprocessing.audio import create_window
from pathlib import Path
import soundfile as sf
import re
from config.paths import PROCESSED_SUBS_DIR, PROCESSED_AUDIO_DIR, PROCESSED_METADATA_DIR



def get_number(file : Path):
    return int(re.search(r"\d+",file.stem).group())



def main():
    subs_files = PROCESSED_SUBS_DIR.glob("*.csv")
    audio_files = PROCESSED_AUDIO_DIR.glob("*.wav")
    audios = {get_number(f): f for f in audio_files}
    subs = {get_number(f): f for f in subs_files}

    for number in sorted(subs.keys() & audios.keys()):
        print(audios[number], subs[number])
        with audios[number].open('r' , encoding="utf-8", newline="") as infile:
            audio , sample_rate= sf.read(infile.name)
            windows = create_window(audio,sample_rate)
            subtitles = load_sub_csv_to_dict(subs[number])

            metadata = map_windows_to_subtitles(windows,subtitles,str(number), f"data/processed/audio/audio{number}.wav")
            with open(f"{PROCESSED_METADATA_DIR}/metadata{number}.json","w",encoding="utf-8") as md:
                json.dump(metadata,md,indent=4,ensure_ascii=False)

if __name__ == "__main__":
    main()
