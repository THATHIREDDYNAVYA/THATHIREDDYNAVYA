import numpy as np
import scipy.io.wavfile as wav

# Read the audio file
rate, data = wav.read('/home/navya/Downloads/Chorus.wav')

# Reverse the audio signal
reversed_data = np.flipud(data)

# Write the reversed audio to a new file
wav.write('/home/navya/Downloads/Chorus.wav', rate, reversed_data)
