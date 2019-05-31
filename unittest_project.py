#!/usr/bin/python3
# https://docs.python.org/3/library/unittest.html
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/30/2019
import unittest
from effects import Effects

class TestAudioMethods(unittest.TestCase):
    def test_echo(self):
        effect = Effects('Hi.wav')
        effect.echo()
        effect.export()

if __name__ == '__main__':
    unittest.main()
