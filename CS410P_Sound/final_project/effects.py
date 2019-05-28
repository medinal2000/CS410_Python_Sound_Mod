# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/21/2019
import sys
import numpy
import scipy.io.wavfile as wavfile
import time

class Effects:
    # Creates four variables sample_rate,left,right,and name
    # left and right are the audio channels
    # name stores the filename for later use
    def __init__(self,filename):
        sample_rate,samples = wavfile.read(filename)
        if len(samples.shape) != 2 or samples.shape[1] != 2:
            print('Stereo Files Only Supported')
            sys.exit(1)
        self.sample_rate = sample_rate
        self.left = samples[:,0]
        self.right = samples[:,1]
        self.original_left = samples[:,0]
        self.original_right = samples[:,1]
        name = filename.split('.')
        self.name = name[0]

    # Exports a wav file based on the altered left and right channels
    # Example $(filename)-Output-$(date and time)
    # Appends current date and time to new file
    def export(self):
        localtime = time.asctime( time.localtime(time.time()) )
        localtime = localtime.replace(' ','-')
        localtime = localtime.replace(':','-')
        self.name = './' + self.name + '-Output-' + localtime + '.wav'
        samples =  numpy.column_stack((self.left,self.right))
        wavfile.write(self.name,self.sample_rate,samples)
        print('Saved File - New Filename: ' + self.name)
        pass

    def normalization(self):
        self.left = self.normalize_channel(self.left)
        self.right = self.normalize_channel(self.right)

    def normalize_channel(self, channel):
        multiplyer = numpy.iinfo(numpy.int16).max
        scale_increase = multiplyer/self.getmax(channel)
        channel = scale_increase * channel
        channel = numpy.floor(channel)
        channel = numpy.array(channel).astype('int16')
        return channel

    def getmax(self, channel):
        return max(channel)

    def audio_delay(self, offset):
        self.left = self.audio_delay_channel(self.left, offset)
        self.right = self.audio_delay_channel(self.right, offset)

    # Takes in Millisecond Input
    def audio_delay_channel(self, channel, offset_ms):
        offset = offset_ms * int(self.sample_rate/1000)
        beginning = numpy.zeros(offset, dtype='int16')
        channel_delay = numpy.append(beginning, channel)
        channel = channel_delay
        return channel


    # Possible Functions
    def compression(self):
        pass

    def tremolo(self):
        pass

    def vibration(self):
        pass

    # Functions to work on
    def echo(self):
        pass

    def reverb(self):
        pass
