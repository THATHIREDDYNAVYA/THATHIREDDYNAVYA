% Writing to a CSV file
data = [1, "John", 25;
        2, "Alice", 30;
        3, "Bob", 28];
csvwrite('data.csv', data);

% Reading from a CSV file
data = csvread('data.csv');
disp("Data read from CSV file:")
disp(data);

% Writing to a binary file (similar to NumPy's .npy format)
array = [1, 2, 3; 4, 5, 6];
save -binary 'data.bin' array;

% Reading from a binary file
fid = fopen('data.bin', 'rb');
loaded_array = fread(fid, 'double');
fclose(fid);
loaded_array = reshape(loaded_array, 3, 2)';
disp("Data loaded from binary file:")
disp(loaded_array);

% Writing to a Pickle-like file (using Octave's own serialization)
dictionary = struct('name', 'John', 'age', 30, 'city', 'New York');
save -binary 'data.pickle' dictionary;

% Reading from a Pickle-like file
load 'data.pickle'
disp("Data loaded from Pickle-like file:")
disp(dictionary);

