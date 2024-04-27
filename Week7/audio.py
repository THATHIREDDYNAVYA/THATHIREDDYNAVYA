import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load audio file
Fs, y = wavfile.read('/home/navya/Downloads/Chorus.wav')

# Plot the signal
t = np.arange(0, len(y)) / Fs
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()
