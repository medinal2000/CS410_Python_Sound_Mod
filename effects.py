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
        # accept stereo audio files only
        self.check_stereo(samples)
        #
        self.sample_rate = sample_rate
        self.left = samples[:,0]
        self.right = samples[:,1]
        self.original_left = samples[:,0]
        self.original_right = samples[:,1]
        # constants
        self.MAX_ECHO = 7
        # save name of file to name output file
        name = filename.split('.')
        self.name = name[0]
        # used for echo functions
        # TODO try to move this to the echo function
        self.echos_left = []
        self.echos_right = []
        # dictionary to map each effects function to the number they
        # correspond to in the interface; keep normalization last
        self.map_to_effects = { '1' : self.apply_all,
                                '2' : self.echo,
                                '3' : self.reverb,
                                '4' : self.normalization
                               }


    # check that the given file is stereo; exit if not
    def check_stereo(self, samples):
        if len(samples.shape) != 2 or samples.shape[1] != 2:
            print('Stereo Files Only Supported')
            sys.exit(1)

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
        print("normalization")
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

    def echo(self, num_of_echos=4):
        self.echo_function(num_of_echos)
        pass

    def echo_function(self,num_of_echos):
        if num_of_echos < 1:
            print('Number of Echos was recvived as a negative number')
            print('Setting Number of Echos to 4')
            num_of_echos = 4
            pass
        elif num_of_echos > self.MAX_ECHO:
            print('Number of Echos was recvived as a number higher then 7')
            print('Setting Number of Echos to 7')
            num_of_echos = self.MAX_ECHO
            pass

        for i in range(0,num_of_echos):
            self.echos_left.insert(i,self.audio_delay_channel(self.original_left,1000*(i+1)))
            self.echos_right.insert(i,self.audio_delay_channel(self.original_right,1000*(i+1)))
            pass

        for i in range(0,num_of_echos):
            self.left = numpy.resize(self.left,self.echos_left[i].shape[0])
            self.right = numpy.resize(self.right,self.echos_right[i].shape[0])
            self.left = numpy.add(self.left,self.echos_left[i])
            self.right = numpy.add(self.right,self.echos_right[i])
            pass
        pass

    def apply_all(self):
        self.echo()
        self.reverb()
        self.normalization()

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
