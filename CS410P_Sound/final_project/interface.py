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

    def run(self, filename):
        repeat = True
        while repeat:
            repeat = self.interface(filename)

    def interface(self, filename):
        self.display_interface()
        requested_effects = self.get_options()
        if not self.validate_input(requested_effects):
            print("You've entered invalid inputs, try again!")
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
        chosen_options = [int(x) for x in user_input.split()]
        return chosen_options

    def validate_input(self, requested_effects):
        for effect in requested_effects:
            if(int(effect) == 1 or int(effect) == 2 or int(effect) == 3
                or int(effect) == 4 or int(effect) == 5):
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
                effects.normalize()
                break
            elif int(e) == 5:
                print("You have opted to exit this program...")
                print("Program exiting, no changes have been made")
                return True
        if normalize:
            effects.normalization()
        return False

    # TODO
    def should_run_again(self):
        return False

