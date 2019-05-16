#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import scipy.io.wavfile as wavfile

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
    # Get the signal file.
    sample_rate,samples = wavfile.read(sys.argv[1])
    return samples

# Main Functions
# The Start of the program
def main():
    samples = getsamples()
    left_samples = samples[:,0]
    right_samples = samples[:,1]
    print(left_samples,right_samples)
    pass

if __name__ == '__main__':
    main()
