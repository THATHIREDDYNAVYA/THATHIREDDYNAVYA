% Define parameters
amplitude = 1;
frequency = 1; % in Hz
phase = 0;
duration = 2; % in seconds
sampling_rate = 1000; % in Hz

% Generate time vector
t = 0:1/sampling_rate:duration;

% Generate sine wave
y = amplitude * sin(2 * pi * frequency * t + phase);

% Plot the sine wave
plot(t, y);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave');
