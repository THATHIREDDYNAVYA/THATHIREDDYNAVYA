import numpy as np
import matplotlib.pyplot as plt

# Define parameters
n = np.arange(0, 20)  # Time index
x = np.random.rand(len(n))  # Original signal x[n]
n0 = 6  # Time shift

# Compute DTFT of x[n]
def dtft(x, n):
    N = len(x)
    k = np.arange(N)
    omega = np.linspace(-np.pi, np.pi, 512)  # Frequency range
    X = np.zeros(len(omega), dtype=complex)
    
    for i, w in enumerate(omega):
        X[i] = np.sum(x * np.exp(-1j * w * n))  # DTFT calculation
    return omega, X

# Compute DTFT of original signal
omega, X = dtft(x, n)

# Create time-shifted signal y[n] = x[n - n0]
n_shifted = n + n0
y = np.zeros(len(n_shifted))
y[n0:] = x[:-n0]  # Shifted signal

# Compute DTFT of shifted signal
omega_shifted, Y = dtft(y, n_shifted)

# Phase shift due to time shift
phase_shift = np.exp(-1j * omega * n0) * X

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('DTFT of Original Signal x[n]')
plt.plot(omega, np.abs(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(ω)|')

plt.subplot(2, 2, 2)
plt.title('DTFT of Shifted Signal y[n]')
plt.plot(omega_shifted, np.abs(Y))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|Y(ω)|')

plt.subplot(2, 2, 3)
plt.title('Phase Shift due to Time Shift')
plt.plot(omega, np.angle(phase_shift), label='Phase Shift')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.legend()

plt.subplot(2, 2, 4)
plt.title('Phase of DTFT of Shifted Signal')
plt.plot(omega_shifted, np.angle(Y), label='Phase of Y(ω)', color='orange')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.legend()

plt.tight_layout()
plt.show()
