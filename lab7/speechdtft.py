import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the WAV file
sampling_rate, data = wavfile.read('/home/navya/Documents/E1:sem-2/compuatational lab/Chorus.wav')

# If stereo, take only one channel
if len(data.shape) > 1:
    data = data[:, 0]

# Normalize the audio data
data = data / np.max(np.abs(data))

# Time axis for the signal
time = np.linspace(0, len(data) / sampling_rate, num=len(data))

# Calculate the DFT
dft = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(data), 1/sampling_rate)

# Plotting the waveform
plt.figure(figsize=(12, 8))

# Time-domain plot
plt.subplot(2, 1, 1)
plt.plot(time, data, color='b')
plt.title('Speech Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()

# Frequency-domain plot
plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], np.abs(dft)[:len(dft)//2], color='r')  # Only plot the positive frequencies
plt.title('DFT of Speech Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
