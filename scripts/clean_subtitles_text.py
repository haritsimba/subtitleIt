import pandas as pd
from config.paths import PROCESSED_SUBS_DIR
from src.preprocessing.subtitles import clean_subtitles_text, clean_sub_formating_tag

def main():
    processed_subs = PROCESSED_SUBS_DIR.glob("*.csv")
    for file in processed_subs:
        clean_sub_formating_tag(file, file)
        df = pd.read_csv(file,header = None,
                names = ["start","end","text","layer"]
            )
        clean_subtitles_text(df)
        df.to_csv(file,index=False, header= False)

if __name__ == "__main__":
    main()