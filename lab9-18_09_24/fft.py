import numpy as np

def fft(x):
    """
    Computes the Fast Fourier Transform (FFT) of the input array x.

    Args:
        x: The input array to be transformed.

    Returns:
        The FFT of the input array.
    """

    N = len(x)
    if N == 1:
        return x

    # Split the input array into even and odd indices
    even = fft(x[::2])
    odd = fft(x[1::2])

    # Compute the twiddle factors
    twiddle = np.exp(-2j * np.pi * np.arange(N // 2) / N)

    # Combine the even and odd components
    return np.concatenate([even + twiddle * odd, even - twiddle * odd])

# Example usage:
x = np.array([1, 2, 3, 4])
X = fft(x)
print(X)