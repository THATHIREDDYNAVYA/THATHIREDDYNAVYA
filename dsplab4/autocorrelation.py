import numpy as np
import matplotlib.pyplot as plt

# Define parameters
N = 64  # Length of the signal
n = np.arange(N)  # Time index
# Create a sample signal (e.g., a simple sinusoidal signal)
x = np.sin(2 * np.pi * 0.1 * n) + 0.5 * np.random.normal(size=N)  # Signal with noise

# Function to compute the DTFT
def dtft(signal):
    N = len(signal)
    omega = np.linspace(-np.pi, np.pi, 512)  # Frequency range
    X = np.zeros(len(omega), dtype=complex)
    
    for i, w in enumerate(omega):
        X[i] = np.sum(signal * np.exp(-1j * w * np.arange(N)))  # DTFT calculation
    return omega, X

# Compute the DTFT of the original signal
omega, X = dtft(x)

# Compute the autocorrelation function
R_x = np.correlate(x, x, mode='full')
R_x = R_x[R_x.size // 2:]  # Keep only the non-negative lags

# Compute the DTFT of the autocorrelation function
omega_R, R_X = dtft(R_x)

# Calculate the squared magnitude of the DTFT of the original signal
squared_magnitude = np.abs(X)**2

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Signal x[n]')
plt.plot(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(2, 2, 2)
plt.title('DTFT of Original Signal |X(ω)|')
plt.plot(omega, np.abs(X))
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('|X(ω)|')

plt.subplot(2, 2, 3)
plt.title('Autocorrelation R_x[n]')
plt.stem(R_x, use_line_collection=True)
plt.xlabel('Lag n')
plt.ylabel('R_x[n]')

plt.subplot(2, 2, 4)
plt.title('DTFT of Autocorrelation |R_X(ω)| and |X(ω)|²')
plt.plot(omega_R, np.abs(R_X), label='|R_X(ω)|')
plt.plot(omega, squared_magnitude, label='|X(ω)|²', linestyle='dashed')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.legend()

plt.tight_layout()
plt.show()
