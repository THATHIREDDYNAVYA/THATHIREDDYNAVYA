import numpy as np
import matplotlib.pyplot as plt

def generate_waves(frequencies, amplitudes, duration, fs):
    t = np.arange(0, duration, 1/fs)
    wave = np.zeros_like(t)
    
    for freq, amp in zip(frequencies, amplitudes):
        wave += amp * np.sin(2 * np.pi * freq * t)
    
    plt.plot(t, wave)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Generated Wave')
    plt.show()

