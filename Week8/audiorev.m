[input_audio, Fs] = audioread('/home/navya/Downloads/Chorus.wav');

% Reverse the audio signal
reversed_audio = flipud(input_audio);

% Write the reversed audio to a new file
audiowrite('/home/navya/Downloads/Chorus.wav', reversed_audio, Fs);

