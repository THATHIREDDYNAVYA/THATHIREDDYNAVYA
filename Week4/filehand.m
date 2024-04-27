% Writing to a file in normal mode
fileID = fopen('data.txt', 'w');
fprintf(fileID, 'Hello, this is a text file.\n');
fclose(fileID);

% Reading from a file in normal mode
fileID = fopen('data.txt', 'r');
data = fread(fileID, '*char');
fclose(fileID);
disp("Data read from file in normal mode:")
disp(data)

% Writing to a file in binary mode
fileID = fopen('data.bin', 'wb');
fwrite(fileID, 'Binary data goes here.');
fclose(fileID);

% Reading from a file in binary mode
fileID = fopen('data.bin', 'rb');
data = fread(fileID, '*char');
fclose(fileID);
disp("Data read from file in binary mode:")
disp(data)
