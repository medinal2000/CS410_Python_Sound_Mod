# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/21/2019

import sys
import numpy
import scipy.io.wavfile as wavfile
import time
import random
import os


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
        # NOTE needs to be here in order to be used by the echo function
        self.echos_left = []
        self.echos_right = []
        # dictionary to map each effects function to the number they
        # correspond to in the interface; keep normalization last
        self.map_to_effects = { '1' : self.apply_all,
                                '2' : self.echo,
                                '3' : self.reverb,
                                '4' : self.speed,
                                '5' : self.normalization
                               }


    # check that the given file is stereo; exit if not
    def check_stereo(self, samples):
        if len(samples.shape) != 2 or samples.shape[1] != 2:
            print('Stereo Files Only Supported')
            sys.exit(1)

    # Exports a wav file based on the altered left and right channels
    # Example $(filename)-Output-$(date and time)
    # Appends current date and time to new file

    # If export is called at the same time,
    # it appends a random letter after Output
    def export(self):
        localtime = time.asctime( time.localtime(time.time()) )
        localtime = localtime.replace(' ','-')
        localtime = localtime.replace(':','-')
        self.output_file = './' + self.name + '-Output-' + localtime + '.wav'
        samples =  numpy.column_stack((self.left,self.right))
        exists = os.path.isfile(self.output_file)
        if not exists:
            wavfile.write(self.output_file,self.sample_rate,samples)
            print('Saved File - New Filename: ' + self.output_file)
        else:
            random_int = random.choice([random.randint(65,90),random.randint(97,122)])
            self.output_file = './' + self.name + '-Output-' + chr(random_int) + '-' + localtime + '.wav'
            wavfile.write(self.output_file,self.sample_rate,samples)
            print('Saved File - New Filename: ' + self.output_file)
        pass

    # Normalizes the audio track
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

    # Begins the process of adding echo to the sound track
    def echo(self, num_of_echos=4, duration_of_echo=1):
        self.num_of_echos = num_of_echos
        self.duration_of_echo = duration_of_echo
        self.duration_of_echo = self.duration_of_echo * 1000
        self.valid_echo()
        self.echo_function()
        pass

    # Adds Echo to the sound track
    def echo_function(self):
        self.echos_left = []
        self.echos_right = []
        for i in range(0,self.num_of_echos):
            self.echos_left.insert(i,self.audio_delay_channel(self.original_left,self.duration_of_echo*(i+1)))
            self.echos_right.insert(i,self.audio_delay_channel(self.original_right,self.duration_of_echo*(i+1)))
            pass

        for i in range(0,self.num_of_echos):
            self.left = numpy.resize(self.left,self.echos_left[i].shape[0])
            self.right = numpy.resize(self.right,self.echos_right[i].shape[0])
            self.left = numpy.add(self.left,self.echos_left[i])
            self.right = numpy.add(self.right,self.echos_right[i])
            pass
        pass

    # Validates Echo Inputs
    def valid_echo(self):
        if self.num_of_echos < 1:
            print('Number of Echos was recvived as a negative number')
            print('Setting Number of Echos to 4')
            self.num_of_echos = 4
            pass
        elif self.num_of_echos > self.MAX_ECHO:
            print('Number of Echos was recvived as a number higher then 7')
            print('Setting Number of Echos to 7')
            self.num_of_echos = self.MAX_ECHO
            pass

        if self.duration_of_echo < 1:
            print('Duration of Echos was recvived less than a second')
            print('Setting Duration of Echos to 1 second')
            self.duration_of_echo = 1
            pass
        pass

    # The Speed functions adjusts the speed the wav file plays out
    def speed(self,duration=0.5):
        self.sample_rate = int(self.sample_rate * duration)
        pass

    # Reverb uses the echo function to generated short echos
    def reverb(self,num_of_reverb=7):
        self.num_of_echos = num_of_reverb
        self.duration_of_echo = 100
        self.valid_reverb()
        self.echo_function()
        pass

    def valid_reverb(self):
        if self.num_of_echos < 1:
            print('Number of Echos was recvived as a negative number')
            print('Setting Number of Echos to 7 in Reverb')
            self.num_of_echos = 7
            pass
        elif self.num_of_echos > self.MAX_ECHO:
            print('Number of Echos was recvived as a number higher then 7')
            print('Setting Number of Echos to 7 in Reverb')
            self.num_of_echos = self.MAX_ECHO
            pass
        pass

    def apply_all(self):
        self.echo()
        self.reverb()
        self.speed()
        self.normalization()
