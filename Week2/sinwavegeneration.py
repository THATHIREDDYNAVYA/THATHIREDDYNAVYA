import numpy as np
import matplotlib.pyplot as plt

# Define parameters
amplitude = 1
frequency = 1  # in Hz
phase = 0
duration = 2  # in seconds
sampling_rate = 1000  # in Hz

# Generate time vector
t = np.arange(0, duration, 1/sampling_rate)

# Generate sine wave
y = amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Plot the sine wave
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.show()

