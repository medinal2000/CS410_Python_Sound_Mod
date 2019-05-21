#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import scipy.io.wavfile as wavfile
import numpy
from effects import Effects


def getsamples():
    # Get the signal file.
    sample_rate,samples = wavfile.read(sys.argv[1])
    return sample_rate,samples

# Main Functions
# The Start of the program
def main():
    effects = Effects()
    sample_rate,samples = getsamples()
    samples = effects.normalization(samples)
    samples = effects.audio_delay(samples, sample_rate, 3000)

    wavfile.write('./test.wav',sample_rate,samples)
    pass

if __name__ == '__main__':
    main()
