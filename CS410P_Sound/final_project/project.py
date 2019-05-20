#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import scipy.io.wavfile as wavfile
import numpy
import audioop

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
    multiplyer = (2**15)-1
    scale_increase = float(multiplyer)/getmax(samples)
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

#might use as a function called by reverb or may rename it as 
#reverb later; could potentially be used for echo too
def audio_delay(samples, sample_rate, offset):
    sample_width = samples.itemsize
    num_bytes_offset = sample_width * offset * int(sample_rate/1000)
    beginning = numpy.zeros(offset, dtype='int16')

    left_samples = samples[:,0]
    right_samples = samples[:,1]
    left_end = samples[:-offset,0]
    right_end = samples[:-offset,1]
    left_delay = numpy.append(beginning, left_end)
    right_delay = numpy.append(beginning, right_end)

    left_samples = left_samples + left_delay
    right_samples = right_samples + right_delay
    return numpy.column_stack((left_samples, right_samples))

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
    samples = audio_delay(samples, sample_rate, 1000)

    wavfile.write('./test.wav',sample_rate,samples)
    pass

if __name__ == '__main__':
    main()
