import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def sampling(x, a):
    """
    Perform upsampling or downsampling on the input signal x based on the factor a.
    
    Parameters:
    x (numpy.ndarray): Input audio signal.
    a (float): Upsampling factor (a > 1) or downsampling factor (a < 1).
    
    Returns:
    numpy.ndarray: Resampled audio signal.
    """
    if a > 1:
        # Upsampling
        upsampled = np.repeat(x, int(a))  # Repeat each sample 'a' times
        return upsampled
    elif a < 1:
        # Downsampling
        downsampled = x[::int(1/a)]  # Take every '1/a' sample
        return downsampled
    else:
        raise ValueError("The value of 'a' must be different from 1.")

def main():
    # Read the audio file
    fs, x = wavfile.read('/home/navya/Documents/E2-SEM1/DSP/DSP LAB/Chorus.wav')
    
    # Get user input for the sampling factor
    a = float(input("Enter the sampling factor (a > 1 for upsampling, a < 1 for downsampling): "))
    
    # Perform sampling
    y = sampling(x, a)
    
    # Plot original and resampled signals
    plt.figure(figsize=(12, 6))
    
    # Original signal
    plt.subplot(2, 1, 1)
    plt.plot(x, color='blue')
    plt.title('Original Audio Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    
    # Resampled signal
    plt.subplot(2, 1, 2)
    plt.plot(y, color='orange')
    plt.title('Resampled Audio Signal (a = {:.2f})'.format(a))
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    plt.show()
    
    # Write the resampled audio to a new file
    wavfile.write('output.wav', int(fs * a), y.astype(np.int16))

if __name__ == "__main__":
    main()
