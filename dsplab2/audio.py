from scipy.io import wavfile

def ds(audio_file, a):
    sample_rate, samples = wavfile.read('/home/navya/Documents/E2-SEM1/DSP/DSP LAB/Chorus.wav')
    if a > 1:
        new_samples = samples[::a]
        new_sample_rate = sample_rate // a
        return new_samples, new_sample_rate

audio_file = r'input.wav'
output_file = r'output.wav'

samples, sample_rate = ds(audio_file, 6)
wavfile.write(output_file, sample_rate, samples)
