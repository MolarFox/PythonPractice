# A password generator - OOP approach

import sys
import random

class PassGen:

    def __init__(self):
        self.pass_length = 0

        # Flags controlling nature of generated passwords
        self.flags = {      
            'incl_uppercase': False,
            'incl_lowercase': False,
            'incl_numbers':   False,
            'incl_symbols':   False
        }

    def _take_bool_input(self, prompt_txt):
        val = input(prompt_txt + " (y/n): ")

        if (val == 'y') or (val == 'Y'):
            return True
        elif (val == 'n') or (val == 'N'):
            return False
        else:
            return None

    
    def collect_specs(self):
        
        # Collect length of password(s) to generate
        input_pending = True
        while input_pending:
            try:

                # Get desired password legnth
                self.pass_length = int (input("Length of generated password(s): "))
                if self.pass_length is None: 
                    raise TypeError

                # Allow uppercase 
                self.flags['incl_uppercase'] = self._take_bool_input(
                    "Include uppercase alphabetic chars?"
                )

                # Allow lowercase
                self.flags['incl_lowercase'] = self._take_bool_input(
                    "Include lowercase alphabetic chars?"
                )

                # Allow numbers
                self.flags['incl_numbers'] = self._take_bool_input(
                    "Include lowercase numeric chars?"
                )

                # Allow symbols
                self.flags['incl_symbols'] = self._take_bool_input(
                    "Include symbols?"
                )

                # Check that the passed bools are all valid, and at least 1 is true
                have_true_param = False
                for key in self.flags:
                    if self.flags[key] is None:
                        raise ValueError
                    have_true_param = have_true_param or self.flags[key]

                if not have_true_param: raise ValueError

            except TypeError:
                print("\nThere was an error with the inputted password length - try again.")
            except ValueError:
                print("\nOne or more flags (y/n) received invalid input, or all were false - try again.")
            else:
                input_pending = False

    def generate(self, count=1):
        while count > 0:
            for _ in range(self.pass_length):
                pass

            count -= 1


if __name__ == '__main__':
    generator = PassGen()

    generator.collect_specs()

    num_to_gen =int(input("Number of passwords to generate: "))
