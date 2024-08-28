import numpy as np

def circular_convolution(x, h):
    """
    Performs circular convolution between two sequences.

    Args:
        x: The first input sequence.
        h: The second input sequence.

    Returns:
        The circular convolution result.
    """

    N = len(x) + len(h) - 1
    x_padded = np.pad(x, (0, N - len(x)), 'constant', constant_values=0)
    h_padded = np.pad(h, (0, N - len(h)), 'constant', constant_values=0)
    y = np.multiply(x_padded, h_padded)
    y_circular = np.fft.ifft(np.fft.fft(y))
    y_result = y_circular[:N]

    return y_result

# Example usage:
x = np.array([1, 2, 3])
h = np.array([4, 5, 6])
result = circular_convolution(x, h)
print(result)