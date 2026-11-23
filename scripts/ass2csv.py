from config.paths import RAW_SUBTITLES_DIR, PROCESSED_SUBS_DIR
from src.preprocessing.subtitles import ass_to_csv

def main():
    ass_subtitles = RAW_SUBTITLES_DIR.glob("*.ass")
    for file in ass_subtitles:
        ass_to_csv(file,PROCESSED_SUBS_DIR)

if __name__ == "__main__" :
    main()