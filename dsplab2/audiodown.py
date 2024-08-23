import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def sampling(x, a):
    if a > 1:
        # Upsampling
        y = np.repeat(x, int(a))
        fs_new = fs * int(a)
    elif a < 1:
        # Downsampling
        y = x[::int(1/a)]
        fs_new = fs // int(1/a)
    else:
        y = x
        fs_new = fs
    return y, fs_new

# Load the audio file
audio_file = "/home/navya/Documents/E2-SEM1/DSP/DSP LAB/Chorus.wav"
fs, data = wavfile.read(audio_file)

# Get the upsampling/downsampling factor from the user
a = float(input("Enter the upsampling/downsampling factor: "))

# Call the sampling function
updown_data, new_fs = sampling(data, a)

# Save the upsampled/downsampled audio
if a > 1:
    output_file = "upsampled_audio.wav"
elif a < 1:
    output_file = "downsampled_audio.wav"
else:
    output_file = "original_audio.wav"

wavfile.write(output_file, new_fs, updown_data.astype(np.int16))

# Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(data)
plt.title('Original Audio')

plt.subplot(3, 1, 2)
plt.plot(updown_data)
plt.title('Sampled Audio')

plt.tight_layout()
plt.show()
