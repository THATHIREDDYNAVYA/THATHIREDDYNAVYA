import numpy as np

def circular_convolution(x, h):
    """
    Calculates the circular convolution of two signals.

    Args:
        x: The first signal.
        h: The second signal.

    Returns:
        The circular convolution of x and h.
    """

    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)), mode='constant')
    h = np.pad(h, (0, N - len(h)), mode='constant')

    X = np.fft.fft(x)
    H = np.fft.fft(h)

    Y = X * H
    y = np.fft.ifft(Y)

    return y

# Example usage
x = np.array([1, 2, 3])
h = np.array([1, -2])

y_circular = circular_convolution(x, h)

# Calculate linear convolution for comparison
y_linear = np.convolve(x, h)

print("Circular Convolution:", y_circular)
print("Linear Convolution:", y_linear)