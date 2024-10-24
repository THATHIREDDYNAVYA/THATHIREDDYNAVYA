import numpy as np
import matplotlib.pyplot as plt

def get_system_parameters():
    """Gets the system parameters from the user."""
    num_zeros = int(input("Enter the number of zeros: "))
    num_poles = int(input("Enter the number of poles: "))

    zeros = []
    for i in range(num_zeros):
        zero = float(input(f"Enter zero {i+1}: "))
        zeros.append(zero)

    poles = []
    for i in range(num_poles):
        pole = float(input(f"Enter pole {i+1}: "))
        poles.append(pole)

    return zeros, poles

def calculate_frequency_response(zeros, poles, frequency_range):
    """Calculates the frequency response of the system."""
    num = np.polyval(zeros, frequency_range * 1j)
    den = np.polyval(poles, frequency_range * 1j)
    response = num / den
    return response

def plot_frequency_response(frequency_range, response, title):
    """Plots the frequency response of the system."""
    plt.figure()
    plt.loglog(frequency_range, np.abs(response))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.grid(True)
    plt.show()

def main():
    """Main function."""
    zeros, poles = get_system_parameters()

    # Create a frequency range from 1 Hz to 1000 Hz
    frequency_range = np.logspace(1, 3, num=1000)

    # Calculate the frequency response
    response = calculate_frequency_response(zeros, poles, frequency_range)

    # Plot the frequency response
    title = f"Frequency Response: {len(zeros)} zeros, {len(poles)} poles"
    plot_frequency_response(frequency_range, response, title)

if __name__ == "__main__":
    main()