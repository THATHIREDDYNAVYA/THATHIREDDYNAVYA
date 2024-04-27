inputFile = '/home/navya/Downloads/Chorus.wav';
outputFile ='/home/navya/Downloads/Chorus.wav';

% Read the audio file
[y, Fs] = audioread(inputFile);

% Reverse the sample order
reversedData = flipud(y);

% Save the reversed audio to a new file
audiowrite(outputFile, reversedData, Fs);

disp('Audio file reversed and saved successfully!');
