import numpy as np
import matplotlib.pyplot as plt

# Define the signals x[n] and h[n]
n = np.arange(-10, 11)  # Discrete time indices
x = np.sinc(n)  # Example signal x[n]: sinc function
h = np.sinc(n / 2)  # Example signal h[n]: scaled sinc function

# Compute the DTFT of x[n]
omega = np.linspace(-np.pi, np.pi, 1000)
X = np.array([np.sum(x * np.exp(-1j * w * n)) for w in omega])

# Compute the DTFT of h[n]
H = np.array([np.sum(h * np.exp(-1j * w * n)) for w in omega])

# Compute the convolution of x[n] and h[n]
conv_result = np.convolve(x, h, mode='full')
n_conv = np.arange(2 * n.min(), 2 * n.max() + 1)

# Compute the DTFT of the convolution result
XH = np.array([np.sum(conv_result * np.exp(-1j * w * n_conv)) for w in omega])

# Verify the convolution property
XH_theoretical = X * H

# Plot the magnitude and phase of the DTFTs to compare
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(omega, np.abs(X), label='|X(e^{jω})|')
plt.title('Magnitude of X(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(omega, np.abs(H), label='|H(e^{jω})|')
plt.title('Magnitude of H(e^{jω})')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(omega, np.abs(XH), label='|XH(e^{jω})|', linestyle='--')
plt.plot(omega, np.abs(XH_theoretical), label='|X(e^{jω}) H(e^{jω})|')
plt.title('Magnitude of Convolution DTFT')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(omega, np.angle(XH), label='∠XH(e^{jω})', linestyle='--')
plt.plot(omega, np.angle(XH_theoretical), label='∠X(e^{jω}) H(e^{jω})')
plt.title('Phase of Convolution DTFT')
plt.xlabel('ω')
plt.ylabel('Phase')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

