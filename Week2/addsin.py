import numpy as np
import matplotlib.pyplot as plt

# Define parameters for first sine wave
amplitude1 = 1
frequency1 = 1  # in Hz
phase1 = 0
duration = 2  # in seconds
sampling_rate = 1000  # in Hz

# Generate time vector
t = np.arange(0, duration, 1/sampling_rate)

# Generate first sine wave
y1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t + phase1)

# Define parameters for second sine wave
amplitude2 = 0.5
frequency2 = 2  # in Hz
phase2 = np.pi/2

# Generate second sine wave
y2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t + phase2)

# Perform addition and subtraction
y_add = y1 + y2
y_sub = y1 - y2

# Plot the resulting waves
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, y_add)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sum of Sine Waves')

plt.subplot(2, 1, 2)
plt.plot(t, y_sub)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Difference of Sine Waves')

plt.tight_layout()
plt.show()
