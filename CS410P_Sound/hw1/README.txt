Name: Medina Lamkin
HOMEWORK 1

For this assignment, I built a demodulator that decoded audio messages.
To start off with, I was very lost, and had no idea how I was supposed 
to do anything. However, after discussing it with classmates, watching
videos online about DSP and the Goertzel algorithm, as well as reading
tips on the slack channel, I was able to complete it. 

I started off by reading the audio file, because that type of stuff is 
familliar to me, then I built the Goertzel filter with a lot of help
from the Moodle resources, and finally I processed the bit stream to get
the separate bytes needed to decode the message. I manually calculated 
the ASCII values that were represented by each byte, so I didn't need 
flip the bits in the bit stream.

In the end, it all went well. I think functionally, all it well with my 
program, however, I didn't make it very modular, nor is it very efficient.
I think I would encapsulate the Goertzel filter in a class as suggested, 
but I would also add more functions as opposed to just writing all my code
at the bottom of my file. Additionally, I do have some hard coded numbers, 
such as the target frequencies. These would need to be cleaned up for better 
coding practices.