import torch
import librosa
import os
import soundfile as sf
import warnings
import time
import sys

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the model
print("Loading model...")
mars5, config_class = torch.hub.load('Camb-ai/mars5-tts', 'mars5_english', trust_repo=True)
print("Model loaded successfully.")

# Function to sanitize file path
def sanitize_path(path):
    return path.strip().replace('\u202a', '').replace('\u202c', '')

# Prompt for reference audio file
while True:
    ref_audio_path = input("Enter the path to the reference audio file (24kHz waveform): ")
    ref_audio_path = sanitize_path(ref_audio_path)
    if os.path.exists(ref_audio_path):
        break
    else:
        print(f"File not found: {ref_audio_path}")
        print("Please check the file path and try again.")

try:
    print("Loading audio file...")
    wav, sr = librosa.load(ref_audio_path, sr=mars5.sr, mono=True)
    wav = torch.from_numpy(wav)
    print("Audio file loaded successfully.")
except Exception as e:
    print(f"Error loading audio file: {e}")
    print("Please ensure the file is a valid audio file and try again.")
    exit(1)

# Prompt for reference transcript
ref_transcript = input("Enter the transcript of the reference audio: ")

# Prompt for deep or shallow clone
deep_clone = input("Do you want a deep clone? (yes/no): ").lower() == 'yes'

# Prompt for configuration settings
top_k = int(input("Enter top_k value (default 100): ") or 100)
temperature = float(input("Enter temperature value (default 0.7): ") or 0.7)
freq_penalty = float(input("Enter frequency penalty value (default 3): ") or 3)

# Create configuration
cfg = config_class(deep_clone=deep_clone, rep_penalty_window=100,
                   top_k=top_k, temperature=temperature, freq_penalty=freq_penalty)

# Prompt for text to synthesize
text_to_synthesize = input("Enter the text to synthesize: ")

# Generate speech
print("Generating speech...")
try:
    # Simple progress indicator
    def progress_indicator():
        while True:
            for char in '|/-\\':
                sys.stdout.write('\r' + 'Processing ' + char)
                sys.stdout.flush()
                time.sleep(0.1)

    import threading
    progress_thread = threading.Thread(target=progress_indicator)
    progress_thread.daemon = True
    progress_thread.start()

    ar_codes, output_audio = mars5.tts(text_to_synthesize, wav, ref_transcript, cfg=cfg)

    # Stop the progress indicator
    progress_thread.do_run = False
    sys.stdout.write('\rProcessing complete!     \n')
except Exception as e:
    print(f"\nError generating speech: {e}")
    exit(1)

# Get the directory of the input file
output_dir = os.path.dirname(ref_audio_path)

# Create output filename
output_filename = f"synthesized_audio_{os.path.basename(ref_audio_path)}"
output_path = os.path.join(output_dir, output_filename)

# Save the output audio
try:
    print("Saving synthesized audio...")
    sf.write(output_path, output_audio.numpy(), mars5.sr)
    print(f"Synthesized audio saved to: {output_path}")
except Exception as e:
    print(f"Error saving audio file: {e}")