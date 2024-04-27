function generate_waves(frequencies, amplitudes, duration, fs)
    t = 0:1/fs:duration;
    wave = zeros(size(t));

    for i = 1:length(frequencies)
        wave = wave + amplitudes(i) * sin(2 * pi * frequencies(i) * t);
    end

    plot(t, wave);
    xlabel('Time (s)');
    ylabel('Amplitude');
    title('Generated Wave');
