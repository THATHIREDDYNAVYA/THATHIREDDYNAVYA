import numpy as np
import matplotlib.pyplot as plt

# Generate a sinusoidal signal
sampling_rate = 1000  # Hz
duration = 1  # seconds
frequency = 50  # Hz
amplitude = 1

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# Sinusoidal signal
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Calculate the DFT
dft = np.fft.fft(signal)
# Frequency bins
frequencies = np.fft.fftfreq(len(signal), 1/sampling_rate)

# Find the maximum peak
max_peak_idx = np.argmax(np.abs(dft))
max_peak_freq = frequencies[max_peak_idx]

# Plotting the signal
plt.figure(figsize=(12, 6))

# Time-domain plot
plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Sinusoidal Signal', color='b')
plt.title('Time Domain Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Frequency-domain plot
plt.subplot(2, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], np.abs(dft)[:len(dft)//2], label='DFT Magnitude', color='r')
plt.axvline(x=max_peak_freq, color='g', linestyle='--', label=f'Max Peak Frequency: {max_peak_freq:.2f} Hz')
plt.title('Frequency Domain (DFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

# Show plots
plt.tight_layout()
plt.show()

print(f"Maximum peak frequency: {max_peak_freq:.2f} Hz")
