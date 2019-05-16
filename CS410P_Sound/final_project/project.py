#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import wave

# Possible Functions
def compression():
    pass

def tremolo():
    pass

def vibration():
    pass

# Functions to work on
def echo():
    pass

def reverb():
    pass

def normalization():
    pass

def getsamples():
    # Get Samples is dervied from
    # Bart Massey findpeak.py
    # https://github.com/pdx-cs-sound/findpeak

    # Get the signal file.
    wavfile = wave.open(sys.argv[1], 'rb')
    # Channels per frame.
    channels = wavfile.getnchannels()
    # Bytes per sample.
    width = wavfile.getsampwidth()
    # Sample rate
    rate = wavfile.getframerate()
    # Number of frames.
    frames = wavfile.getnframes()
    # Length of a frame
    frame_width = width * channels
    # Get the signal and check it
    wave_bytes = wavfile.readframes(frames)
    # Iterate over frames.
    samples = []
    for f in range(0, len(wave_bytes), frame_width):
        frame = wave_bytes[f : f + frame_width]
        # Iterate over channels.
        for c in range(0, len(frame), width):
            # Build a sample.
            sample_bytes = frame[c : c + width]
            # XXX Eight-bit samples are unsigned
            sample = int.from_bytes(sample_bytes,
            byteorder='little',
            signed=(width>1))
            samples.append(sample)
    return samples

# Main Functions
# The Start of the program
def main():
    samples = getsamples()
    print(samples)
    pass

if __name__ == '__main__':
    main()
