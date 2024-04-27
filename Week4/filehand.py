# Writing to a file in normal mode
with open('data.txt', 'w') as file:
    file.write('Hello, this is a text file.\n')

# Reading from a file in normal mode
with open('data.txt', 'r') as file:
    data = file.read()
    print("Data read from file in normal mode:")
    print(data)

# Writing to a file in binary mode
with open('data.bin', 'wb') as file:
    file.write(b'Binary data goes here.')

# Reading from a file in binary mode
with open('data.bin', 'rb') as file:
    data = file.read()
    print("\nData read from file in binary mode:")
    print(data)
