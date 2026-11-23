from config.paths import RAW_ANIME_DIR, PROCESSED_AUDIO_DIR
from src.preprocessing.audio import extract_audio


def main():
    videos = RAW_ANIME_DIR.glob("*.mp4")
    for file in videos:
        output_name = file.with_suffix(".wav").name.replace('vid','audio')
        extract_audio(file,PROCESSED_AUDIO_DIR / output_name)

if __name__ == "__main__":
    main()