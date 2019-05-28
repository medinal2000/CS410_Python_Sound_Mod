import os
from effects import Effects

class CmdInterface():
    def __init__(self):
        self.options = {'1' : 'Normalization',
                        '2' : 'Echo',
                        '3' : 'Reverb',
                        '4' : 'Apply all effects',
                        '5' : 'Exit'
                        }
        pass

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

    # TODO make it ensure file is wav file
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

    def interface(self, filename):
        self.display_interface()
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

    def display_interface(self):
        print("Here are the available effects you can add to your audio file:")
        for key in self.options:
            print(key,": ", self.options[key])
        print("Type in a space delimited list of numbers corresponding effects you would like applied.")
        pass

    def get_options(self):
        user_input = input()
        chosen_options = [x for x in user_input.split()]
        return chosen_options

    def validate_input(self, requested_effects):
        for effect in requested_effects:
            if(effect == '1' or effect == '2' or effect == '3'
                or effect == '4' or effect == '5'):
                return True
            else:
                return False

    # returns a boolean value indicating whether user opted to quit or not 
    def apply_effects(self, filename, requested_effects):
        effects = Effects(filename)
        # if user wants to normalize the audio, it will be done at the very end
        normalize = False
        for e in requested_effects:
            if int(e) == 1:
               normalize = True
            elif int(e) == 2:
                effects.echo()
            elif int(e) == 3:
                effects.reverb()
            elif int(e) == 4:
                effects.echo()
                effects.reverb()
                effects.normalization()
                break
            elif int(e) == 5:
                print("You have opted to exit this program...")
                print("Program exiting, no changes have been made")
                return True
        if normalize:
            effects.normalization()
        # save the altered version of the wave file
        effects.export()
        return False

    # TODO
    def should_run_again(self):
        return False

