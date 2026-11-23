import subprocess
from pathlib import Path
import soundfile as sf
import numpy as np

def extract_audio(input_path : Path, output_path : Path) -> None :
    command = ["ffmpeg",
               "-i", f"{input_path}" ,
               "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "1",
               f"{output_path}"]
    subprocess.run(command,check=True)

def create_window(audio, sample_rate, duration=10, overlap=2):
    window_size = int(duration * sample_rate)
    step_size = int((duration - overlap) * sample_rate)
    windows = []
    for start in range(0, len(audio) - window_size+1,step_size):
        end = start + window_size
        windows.append({
            "start": start / sample_rate,
            "end" : end / sample_rate,
            "audio" : audio[start:end]
        })
    return windows

