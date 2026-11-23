import json
from config.paths import PROCESSED_DIR, PROJECT_ROOT

metadatas = PROCESSED_DIR.glob("*.json")
def load_dataset():
    samples = []
    for json_file in sorted(metadatas) :
        with json_file.open("r",encoding="utf-8") as f:
          metadata = json.load(f)
          for sample in metadata:
              sample["audio_path"] = PROJECT_ROOT / sample["audio_path"]
              samples.extend(metadata)
    return samples