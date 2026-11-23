import os
import subprocess
import sys
from config.paths import PREPROCESSING_SCRIPTS_DIR, PROJECT_ROOT

STEPS = [
    ("Extract audio" , "extract_audio.py"),
    ("Convert ass to CSV","ass2csv.py"),
    ("Clean subtitles", "clean_subtitles_text.py"),
    ("Map audio windows to corresponding subtitles","map_win_to_sub.py")
]

def run_preprocessing():
    for step_name, script_name in STEPS:
        script_path = PREPROCESSING_SCRIPTS_DIR / script_name
        print(f"\n{'=' * 50}")
        print(f"starting : {step_name}")
        print(f"{'=' * 50}")
        try:
            subprocess.run([sys.executable, str(script_path)], cwd=PROJECT_ROOT, check=True)
        except subprocess.CalledProcessError as error:
            print(f"\nERROR : {step_name} failed!")
            print(f"Exit code : {error.returncode}")
            print("Preprocessing stoped.")
            sys.exit(error.returncode)
        except FileNotFoundError:
            print(f"\nERROR : Script not found : {script_path}")
            sys.exit(1)
        print(f"Successfully completed: {step_name}")
    print("\nAll preprocessing steps completed successfully")

if __name__ == "__main__" :
    run_preprocessing()
