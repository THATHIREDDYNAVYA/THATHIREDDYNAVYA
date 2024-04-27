import csv
import numpy as np
import pickle

# Writing to a CSV file
data = [[1, 'John', 25],
        [2, 'Alice', 30],
        [3, 'Bob', 28]]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Reading from a CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Writing to a NumPy binary file
array = np.array([[1, 2, 3], [4, 5, 6]])
np.save('data.npy', array)

# Reading from a NumPy binary file
loaded_array = np.load('data.npy')
print("\nData loaded from NumPy binary file:")
print(loaded_array)

# Writing to a Pickle file
dictionary = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.pkl', 'wb') as file:
    pickle.dump(dictionary, file)

# Reading from a Pickle file
with open('data.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)
    print("\nData loaded from Pickle file:")
    print(loaded_dict)
