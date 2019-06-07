#!/usr/bin/python3
# https://docs.python.org/3/library/unittest.html
# Final Project for CS410P
# By: Ebraheem AlAthari and Medina Lamkin
# Date: 05/30/2019
import unittest
from effects import Effects

class TestAudioMethods(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.effect = Effects('Hello.wav')

    def test_echo(cls):
        print("Echo Test")
        cls.effect.echo()

    def test_reverb(cls):
        print("Reverb Test")
        cls.effect.reverb()
        pass

    def test_speed(cls):
        print("Speed Test")
        cls.effect.speed()
        pass

    def test_normalization(cls):
        print("normalization Test")
        cls.effect.normalization()
        pass

    @classmethod
    def tearDown(cls):
        cls.effect.export()

if __name__ == '__main__':
    unittest.main()
