#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import scipy.io.wavfile as wavfile
import numpy

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

def normalization(samples):
    multiplyer = numpy.iinfo(numpy.int16).max
    scale_increase = multiplyer/getmax(samples)
    left_samples = samples[:,0]
    right_samples = samples[:,1]
    left_samples = scale_increase * left_samples
    right_samples = scale_increase * right_samples
    left_samples = numpy.floor(left_samples)
    right_samples = numpy.floor(right_samples)
    left_samples = numpy.array(left_samples).astype('int16')
    right_samples = numpy.array(right_samples).astype('int16')

    samples =  numpy.column_stack((left_samples,right_samples))
    return samples

def getmax(samples):
    left_samples = samples[:,0]
    left_max = max(left_samples)
    right_samples = samples[:,1]
    right_max = max(right_samples)
    max_sample = 0
    if left_max > right_max:
        max_sample = left_max
        pass
    else:
        max_sample = right_max
    return max_sample

def getsamples():
    # Get the signal file.
    sample_rate,samples = wavfile.read(sys.argv[1])
    return sample_rate,samples

# Main Functions
# The Start of the program
def main():
    sample_rate,samples = getsamples()
    samples = normalization(samples)
    wavfile.write('./test.wav',sample_rate,samples)
    pass

if __name__ == '__main__':
    main()
