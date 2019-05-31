#!/usr/bin/python3
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/30/2019
from interface import CmdInterface
from effects import Effects
def main():
    effect = Effects('Hi.wav')
    effect.echo()
    effect.normalization()
    effect.export()
    pass

if __name__ == '__main__':
    main()
