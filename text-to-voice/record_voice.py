import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Recording settings
sample_rate = 44100  # Sample rate (in Hz)
duration_seconds = 5  # Duration of recording (in seconds)
output_filename = "recorded_audio.wav"

print(f"Recording for {duration_seconds} seconds...")

# Record audio from the default input device
# The output is a NumPy array
audio_data = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=2)

# Wait until the recording is finished
sd.wait()

print("Recording complete.")

# Save the recorded audio to a WAV file
write(output_filename, sample_rate, audio_data)

print(f"Audio saved to {output_filename}")


