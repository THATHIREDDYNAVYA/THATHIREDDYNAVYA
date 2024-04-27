% Define parameters for first sine wave
amplitude1 = 1;
frequency1 = 1; % in Hz
phase1 = 0;
duration = 2; % in seconds
sampling_rate = 1000; % in Hz

% Generate time vector
t = 0:1/sampling_rate:duration;

% Generate first sine wave
y1 = amplitude1 * sin(2 * pi * frequency1 * t + phase1);

% Define parameters for second sine wave
amplitude2 = 0.5;
frequency2 = 2; % in Hz
phase2 = pi/2;

% Generate second sine wave
y2 = amplitude2 * sin(2 * pi * frequency2 * t + phase2);

% Perform addition and subtraction
y_add = y1 + y2;
y_sub = y1 - y2;

% Plot the resulting waves
subplot(2,1,1);
plot(t, y_add);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sum of Sine Waves');

subplot(2,1,2);
plot(t, y_sub);
xlabel('Time (s)');
ylabel('Amplitude');
title('Difference of Sine Waves');
