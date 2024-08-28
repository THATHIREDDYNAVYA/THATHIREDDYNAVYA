def circular_shift(lst, shift):
    n = len(lst)
    # Ensure the shift is within the length of the list
    shift = shift % n
    
    # Perform the circular shift
    return lst[-shift:] + lst[:-shift]

# Test the function
example_list = [1, 2, 3, 4, 5]

# Circular shift to the right by 2 positions
print(circular_shift(example_list, 2))  # Output: [4, 5, 1, 2, 3]

# Circular shift to the left by 2 positions
print(circular_shift(example_list, -2))  # Output: [3, 4, 5, 1, 2]