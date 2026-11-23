import re
from pathlib import Path
import pysubs2
import csv
import pandas as pd


def ass_to_csv(ass_file : Path,output_directory :Path = None):
    subs = pysubs2.load(str(ass_file))
    if output_directory is None:
        output_directory = ass_file.parent
    csv_name = ass_file.with_suffix(".csv").name
    output_file = output_directory / csv_name
    with output_file.open("w", newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        for line in subs:
            writer.writerow([
                line.start / 1000,
                line.end / 1000,
                line.text,
                line.layer
            ])
    return output_file


def clean_formating_tags(text : str) -> str :
    text  = re.sub(r'\{[^}]*\}','',text)
    text = re.sub(r'\s+',' ',text)
    return text.strip()

def clean_sub_formating_tag(sub_csv_path:Path, output_file: Path):
    with sub_csv_path.open("r",encoding="utf-8",newline="") as infile:
        reader = csv.reader(infile)
        rows = []
        for row in reader:
            if len(row) >= 3:
                row[2] = clean_formating_tags(row[2])
            rows.append(row)
    with output_file.open("w",encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

def clean_subtitles_text(df):
    df["text"] = df["text"].str.replace(r"\\N"," ", regex=True)
    return df

def load_sub_csv_to_dict(csv_path : Path):
    df = pd.read_csv(
        csv_path,
        header = None,
        names = ["start","end","text","layer"]
    )
    df["start"] = pd.to_numeric(df["start"])
    df["end"] = pd.to_numeric(df["end"])
    return df.to_dict(orient="records")