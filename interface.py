import os
from effects import Effects

class CmdInterface():
    def __init__(self):
        # option values; allows for less hard coding of values
        self.all, self.echo = '1', '2'
        self.reverb, self.normalize = '3', '4'
        self.quit = '5'
        # dictionary to map each option to its desciption
        self.options = {self.all : 'Apply all effects',
                        self.echo : 'Echo',
                        self.reverb : 'Reverb',
                        self.normalize : 'Normalization',
                        self.quit : 'Don\'t apply any effects (program will exit)'
                        }
        self.users_choices = {self.all : False,
                              self.echo : False,
                              self.reverb : False,
                              self.normalize : False
                              }
        print(self.users_choices)
        pass

    # get filename and run the program
    def run(self):
        # get a wave file to edit
        filename = self.get_filename()
        while not self.validate_filename(filename):
            filename = self.get_filename()
        # run the program on a given wav file
        repeat = True
        while repeat:
            repeat = self.interface(filename)
        pass

    def get_filename(self):
        filename = input("Please enter the name of a wav file you'd like to modify: ")
        return filename

    # ensures file exists and is a wav file
    def validate_filename(self, filename):
        exists = os.path.isfile(filename)
        if not exists:
            print('File: ' + filename + ' can\'t be found')
            return exists
        else:
            if filename.endswith('.wav'):
                return True
            else:
                print("Your file is not a wav file, please enter the name of a wav file along with the '.wav' extension.")
                return False

    # displays the interactive UI once
    def interface(self, filename):
        self.display_options()
        requested_effects = self.get_options()
        if not self.validate_input(requested_effects):
            print("You've entered invalid inputs, try again with a number 1-5!")
            repeat = True
            return repeat
        quit = self.apply_effects(filename, requested_effects)
        if not quit:
            repeat = self.should_run_again()
        else:
            repeat = False
        return repeat

    def display_options(self):
        print("\nHere are the available effects you can add to your audio file:")
        for key in self.options:
            print(key,": ", self.options[key])
        print("Type in a space delimited list of numbers corresponding effects you would like applied.")
        pass

    def get_options(self):
        user_input = input()
        chosen_options = [x for x in user_input.split()]
        return chosen_options

    # validate the file modification options user entered
    def validate_input(self, requested_effects):
        for effect in requested_effects:
            if(effect == self.all or effect == self.echo or effect == self.reverb
                or effect == self.normalize or effect == self.quit):
                return True
            else:
                return False

    # returns a boolean value indicating whether user opted to quit or not 
    def apply_effects(self, filename, requested_effects):
        effects = Effects(filename)
        # decide what the user has opted to do
        for e in requested_effects:
            # user has opted to quit program
            if e == self.quit:
                return True
            # if not quiting, record what user wants
            self.users_choices[e] = True
            # if user want to apply all effects, no need to continue looping
            if e == self.all:
                break
        # apply the effects
        for option in self.users_choices.items():
            if option[1] == True:
                print(option, "effect will apply")
        # save the altered version of the wav file
        effects.export()
        return False

    # ask the user if they wish to edit their wav file again
    def should_run_again(self):
        answer = input("\nWould you like to change your wav file again? (Y/N)\n")
        if (answer == 'Y' or answer == 'y' or answer.lower() == 'yes'):
            return True
        else:
            return False

