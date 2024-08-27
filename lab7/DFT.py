import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define an arbitrary signal
# For demonstration, let's create a signal composed of two sinusoidal waves
N = 256  # Number of samples
t = np.arange(N)
freq1 = 5  # Frequency of the first sine wave
freq2 = 20  # Frequency of the second sine wave
signal = np.sin(2 * np.pi * freq1 * t / N) + 0.5 * np.sin(2 * np.pi * freq2 * t / N)

# Step 2: Compute the DFT of the signal
def dft(signal):
    N = len(signal)
    X = np.zeros(N, complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Compute DFT
X = dft(signal)

# Step 3: Calculate magnitude and phase
magnitude = np.abs(X)
phase = np.angle(X)

# Step 4: Plot magnitude and phase
freq = np.arange(N)  # Frequency bins

plt.figure(figsize=(12, 6))

# Plot magnitude spectrum
plt.subplot(2, 1, 1)
plt.plot(freq, magnitude)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

# Plot phase spectrum
plt.subplot(2, 1, 2)
plt.plot(freq, phase)
plt.title('Phase Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()
