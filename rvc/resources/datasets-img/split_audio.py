import sys
import os
from tqdm import tqdm
import numpy as np
import librosa
from scipy import signal
from scipy.io import wavfile

def run_split(input_path, output_path, sr, chunk_len=3.0, overlap_len=0.3):
    # Load the audio file
    audio, sr = librosa.load(input_path, sr=sr, res_type='soxr_vhq')
    
    # Apply a high-pass filter
#    b_high, a_high = signal.butter(N=5, Wn=48, btype="high", fs=sr)
#    audio = signal.lfilter(b_high, a_high, audio)
    
    chunk_length = int(sr * chunk_len)
    overlap_length = int(sr * overlap_len)
    
    with tqdm(total=len(audio)// (chunk_length - overlap_length), leave=False) as pbar:
        i = 0
        while i < len(audio):
            # Extract the chunk
            chunk = audio[i:i + chunk_length]
            
            # Only save the chunk if it meets the minimum length requirement
            if len(chunk) == chunk_length:
                chunk_filename = os.path.join(output_path, f"chunk_{i // (chunk_length - overlap_length):04}.wav")
                wavfile.write(chunk_filename, sr, chunk.astype(np.float32))
                
            # Update the index for the next chunk with overlap
            i += chunk_length - overlap_length
            pbar.update(1)

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    sr = int(sys.argv[3])
    chunk_len = float(sys.argv[4])
    overlap_len = float(sys.argv[5])
    run_split(input_path=input_path, output_path=output_path, sr=sr, chunk_len=chunk_len, overlap_len=overlap_len)