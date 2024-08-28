import numpy as np

def dft(sequence):
    N = len(sequence)
    result = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            result[k] += sequence[n] * np.exp(-2j * np.pi * k * n / N)
    return result

def idft(sequence):
    N = len(sequence)
    result = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            result[n] += sequence[k] * np.exp(2j * np.pi * k * n / N)
    return result / N

def circular_convolution_dft(x, h):
    # Ensure both sequences are the same length by padding the shorter one
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')

    # Compute the DFT of both sequences using the custom DFT function
    X = dft(x)
    H = dft(h)

    # Perform point-wise multiplication in the frequency domain
    Y = X * H

    # Compute the inverse DFT to get the circular convolution result
    y = idft(Y)

    return np.real(y)  # Return the real part of the result

# Example usage:
x = np.array([1, 2, 3, 4])   # First input sequence
h = np.array([0, 1, 0.5, 0.5])  # Second input sequence

# Perform circular convolution using DFT and IDFT
output_dft = circular_convolution_dft(x, h)
print("Circular Convolution Result (DFT without FFT):", output_dft)

# Perform circular convolution using direct method for comparison
def circular_convolution_direct(x, h):
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')
    result = np.zeros(N)
    for n in range(N):
        for m in range(N):
            result[n] += x[m] * h[(n - m) % N]
    return result

output_direct = circular_convolution_direct(x, h)
print("Circular Convolution Result (Direct):", output_direct)