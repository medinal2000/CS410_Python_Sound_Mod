#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/16/2019
from interface import CmdInterface
from effects import Effects
import sys

# Main Function
# The Start of the program
# Adds Effects to the file
def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'debug':
        effect = Effects('Hello.wav')
        effect.echo()
        effect.normalization()
        effect.export()
    else:
        interface = CmdInterface()
        interface.run()

if __name__ == '__main__':
    main()
