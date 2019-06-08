## Copyright (c) 2019 Medina Lamkin, Ebraheem AlAthari


For this project, we built an application that allows the user to modify
audio files of their choices. This application has a command line interface,
and may be used as described in the README.md (or by simply running "python3
project.py"). Initially, it was very difficult getting started, as neither of
us have any experience with working with sound or manipulating it. The initial
learning curve was difficult to overcome.

At the time of submitting our project proposal, we had no idea of what to
really expect from taking on our proposed project. In the proposal, we had
written about building a sound modifier that would make music recordings sound
more professional. However, through trying to implement such an application,
it was funner to work with voice files, especially since neither of us have a
strong passion for music production, where the proposed application would have
been very helpful.

We ended up building an Effects class which just applies some effect to a given
wavfile. While this might be able to improve the quality of music audio files,
I am mentioning this, as it has yet to be tested on recordings of music. Most
of our testing of these effects was done on simple audio files (some of which
are included in the repository).

The application allows users to specify the effects they would like applied to
their audio file. This application could also be used to help people who are
unfamilliar with what the different audio effects do learn about these effects.
There are four effects currently implemented: echo, reverb, normalization,
and speed (changes how quickly audio file plays). Of the effects we had
initially planned on implementing, we were only unsuccessful at implementing
one effect - compression.

We had hoped that we might be able to implement a more complex interface that
would allow users to set the parameters of the various effects, however, we
were aware of the lack of time available to us and opted to focus on building
the effects rather than implementing another interface. This is something that
we would like to continue working on after the end of the course. We hope to
make it a graphical interface rather than a text interface to make it easier
to use and more accessible to all sorts of people.

This is the tool we are considering using to build the GUI:
https://wiki.python.org/moin/TkInter

Overall, we think that our final application works well. While it is definitely
no where near as impressive as the projects of some other groups (aka, everyone
who demoed their projects), we feel that we have learned a tremendous amount
about audio and audio file processing/manipulation during the past couple of
weeks. Throughout this process, we have grown to respect the complexity of
audio.
