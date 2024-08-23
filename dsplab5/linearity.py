import numpy as np

def dtft(x, omega):
    # Create an empty array to hold the result
    result = np.zeros_like(omega, dtype=complex)
    
    # Loop over each frequency
    for k, freq in enumerate(omega):
        # Compute the DTFT at this frequency
        result[k] = np.sum(x * np.exp(-1j * freq * np.arange(len(x))))
    
    return result

# Define signals
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])  # Fixed the syntax error
x3 = x2 + x1  # Combined signal

# Define frequencies
omega = np.array([0, np.pi/4, np.pi/2])

# Compute DTFTs
X1 = dtft(x1, omega)
X2 = dtft(x2, omega)
X = dtft(x3, omega)
X3 = X2 + X1

# Print results
print("DTFT of x1:", X1)
print("DTFT of x2:", X2)
print("DTFT of x3:", X)
print("Sum of DTFTs X1 + X2:", X3)

# Check if linearity property is satisfied
if np.allclose(X, X3):
    print("Linearity property is proved")
else:
    print("Linearity property is not proved")

