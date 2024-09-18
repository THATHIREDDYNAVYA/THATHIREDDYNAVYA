import numpy as np
import matplotlib.pyplot as plt

# Sample parameters
sampling_rate = 1000  # Hz
t = np.linspace(0, 1.0, sampling_rate)  # Time vector for 1 second

# Create a sample signal (sine wave with frequency 50 Hz)
frequency = 50  # Hz
signal = np.sin(2 * np.pi * frequency * t)

# Create an exponential function (e^(-alpha * t))
alpha = 5  # Decay constant
exponential = np.exp(-alpha * t)

# Multiply the signal with the exponential
modified_signal = signal * exponential

# Plot the original sine signal, the exponential, and the result signal
plt.figure(figsize=(12, 8))

# Plot original sine signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Sine Signal')
plt.title('Original Sine Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot exponential function
plt.subplot(3, 1, 2)
plt.plot(t, exponential, label='Exponential Decay', color='green')
plt.title('Exponential Decay (e^(-alpha * t))')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the resulting signal (sine * exponential)
plt.subplot(3, 1, 3)
plt.plot(t, modified_signal, label='Resulting Signal', color='orange')
plt.title('Resulting Signal (Sine * Exponential)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()