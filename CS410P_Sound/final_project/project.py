#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
import sys
import os
from interface import CmdInterface 
from effects import Effects

# Checks if file exists and if not stops the program
def validate_file(filename):
    exists = os.path.isfile(filename)
    if not exists:
        print('File: ' + filename + ' can\'t be found')
        sys.exit(1)

# Main Function
# The Start of the program
# Adds Effects to the file
def main(filename):
    validate_file(filename)
    alter_wav_file = Effects(filename)
    alter_wav_file.audio_delay(3000)
    alter_wav_file.normalization()
    alter_wav_file.export()
    interface = CmdInterface()
    interface.run(filename)

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
