% Writing to a text file
data = [1, 2, 3; 4, 5, 6; 7, 8, 9];
dlmwrite('data.txt', data);

% Reading from a text file
data = dlmread('data.txt');
disp('Data read from text file:');
disp(data);

% Writing to a binary file
array = [10, 20, 30];
fid = fopen('data.bin', 'wb');
fwrite(fid, array, 'double');
fclose(fid);

% Reading from a binary file
fid = fopen('data.bin', 'rb');
loaded_array = fread(fid, Inf, 'double');
fclose(fid);
disp('Data read from binary file:');
disp(loaded_array);
