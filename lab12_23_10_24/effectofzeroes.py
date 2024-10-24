import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Function to calculate the frequency response of a system with zeros
def frequency_response(num_zeros, den_coeffs, num_points=512):
    # Calculate the frequency response using freqz
    w, h = freqz(num_zeros, den_coeffs, worN=num_points)
    return w, h

# User inputs
num_zeros = list(map(float, input("Enter the coefficients of the numerator (zeros) separated by space: ").split()))
den_coeffs = list(map(float, input("Enter the coefficients of the denominator (poles) separated by space: ").split()))

# Calculate frequency response
frequencies, response = frequency_response(num_zeros, den_coeffs)

# Plotting the frequency response
plt.figure(figsize=(12, 6))
plt.plot(frequencies / np.pi, 20 * np.log10(np.abs(response)), 'b')
plt.title('Frequency Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axhline(0, color='red', linestyle='--')
plt.show()