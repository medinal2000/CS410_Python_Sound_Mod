# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/21/2019
import sys
import numpy
import scipy.io.wavfile as wavfile
import time
MAX_ECHO = 7


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
        self.echos_left = []
        self.echos_right = []

    # Exports a wav file based on the altered left and right channels
    # Example $(filename)-Output-$(date and time)
    # Appends current date and time to new file
    def export(self):
        localtime = time.asctime( time.localtime(time.time()) )
        localtime = localtime.replace(' ','-')
        localtime = localtime.replace(':','-')
        self.output_file = './' + self.name + '-Output-' + localtime + '.wav'
        samples =  numpy.column_stack((self.left,self.right))
        wavfile.write(self.output_file,self.sample_rate,samples)
        print('Saved File - New Filename: ' + self.output_file)
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

    def echo(self):
        self.echo_function(4)
        pass

    def echo_function(self,num_of_echos):
        global MAX_ECHO
        if num_of_echos < 1:
            print('Number of Echos was recvived as a negative number')
            print('Setting Number of Echos to 4')
            num_of_echos = 4
            pass
        elif num_of_echos > MAX_ECHO:
            print('Number of Echos was recvived as a number higher then 7')
            print('Setting Number of Echos to 7')
            num_of_echos = MAX_ECHO
            pass
        for i in range(0,num_of_echos):
            self.echos_left.insert(i,self.audio_delay_channel(self.original_left,2000*(i+1)))
            self.echos_right.insert(i,self.audio_delay_channel(self.original_right,2000*(i+1)))
            pass

        for i in range(0,num_of_echos):
            self.left = numpy.append(self.left,self.echos_left[i])
            self.right = numpy.append(self.right,self.echos_right[i])
            pass
        pass


    # Possible Functions
    def compression(self):
        pass

    def tremolo(self):
        pass

    def vibration(self):
        pass

    # Functions to work on
    def reverb(self):
        pass
