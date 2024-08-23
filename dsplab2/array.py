import numpy as np
import matplotlib.pyplot as plt

# Get array input from the user
user_input = input("Enter the array elements separated by spaces: ")
arr = np.array([float(x) for x in user_input.split()])

print("\nOriginal array:")
print(arr)

# Upsampling the array
upsampled_arr = np.repeat(arr, 4)
print("\nUpsampled array:")
print(upsampled_arr)

# Downsampling the array
downsampled_arr = arr[::4]
print("\nDownsampled array:")
print(downsampled_arr)

# Plotting the arrays
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(arr, 'ro-')
plt.title('Original Array')

plt.subplot(3, 1, 2)
plt.plot(upsampled_arr, 'go-')
plt.title('Upsampled Array')

plt.subplot(3, 1, 3)
plt.plot(downsampled_arr, 'bo-')
plt.title('Downsampled Array')

plt.tight_layout()
plt.show()
