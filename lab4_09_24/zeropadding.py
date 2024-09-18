import numpy as np
import matplotlib.pyplot as plt

# Original signal
x = np.array([1, 2, 3, 4,5,6,])

# 4-point DFT (original signal)
X0 = np.fft.fft(x)


X1 = np.fft.fft(np.pad(x, (0, 4), 'constant'))


X2 = np.fft.fft(np.pad(x, (0, 10), 'constant'))

# Magnitude spectrums
mag_X0 = np.abs(X0)
mag_X1 = np.abs(X1)
mag_X2 = np.abs(X2)

# Plotting
plt.figure(figsize=(15, 8))
plt.subplot(3, 1, 1)
plt.stem(mag_X0)
plt.title('4-point DFT Magnitude Spectrum (Original Signal)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 2)
plt.stem(mag_X1)
plt.title('6-point DFT Magnitude Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 3)
plt.stem(mag_X2)
plt.title('12-point DFT Magnitude Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()