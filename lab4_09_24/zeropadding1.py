import numpy as np
import matplotlib.pyplot as plt

# Function to compute DFT manually
def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Original signal
N = 16  # Original number of points
t = np.arange(N)
signal = np.sin(2 * np.pi * t / N)  # A simple sinusoidal signal

# Compute DFT without zero-padding
dft_signal = dft(signal)

# Zero-pad the signal
zero_padded_signal = np.pad(signal, (0, N*3), 'constant')  # Zero-pad to 4 times the original length

# Compute DFT with zero-padding
dft_zero_padded = dft(zero_padded_signal)

# Frequency axis
freq = np.arange(N)
freq_padded = np.arange(len(zero_padded_signal))

# Plot the original DFT
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.stem(freq, np.abs(dft_signal), 'b', markerfmt=" ", basefmt="-b")
plt.title('DFT without Zero Padding')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

# Plot the zero-padded DFT
plt.subplot(1, 2, 2)
plt.stem(freq_padded, np.abs(dft_zero_padded), 'r', markerfmt=" ", basefmt="-r")
plt.title('DFT with Zero Padding')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()