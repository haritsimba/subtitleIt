from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

PREPROCESSING_SCRIPTS_DIR = PROJECT_ROOT / "scripts"

RAW_DIR = DATA_DIR / "raw"
RAW_ANIME_DIR = RAW_DIR / "animes"
RAW_SUBTITLES_DIR = RAW_DIR / "subs"

PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_AUDIO_DIR = PROCESSED_DIR / "audio"
PROCESSED_METADATA_DIR = PROCESSED_DIR / "metadata"
PROCESSED_SUBS_DIR = PROCESSED_DIR / "subtitles"