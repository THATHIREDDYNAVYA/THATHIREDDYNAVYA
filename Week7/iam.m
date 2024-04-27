% Load audio file
[y, Fs] = audioread('/home/navya/Downloads/Chorus.wav');
% Plot the signal
t = (0:length(y)-1) / Fs;
plot(t, y);
xlabel('Time (s)');
ylabel('Amplitude');
title('Audio Signal');

