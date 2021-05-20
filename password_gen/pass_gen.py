# A password generator - OOP approach
# MolarFox 2021

import sys
import random

# Defines ascii character ranges as nested tuples
CHAR_RANGES = (
    (65, 90),   # uppercase alphas
    (97, 122),  # lowercase alphas
    (48, 57),   # numbers
    (58, 64)    # symbols only some, for simplicity
)

class PassGen:
    """Password generator class"""

    def __init__(self):
        """Initialises password generator class variables"""
        self.pass_length = 0

        # Flags controlling nature of generated passwords
        self.flags = {      
            'incl_uppercase': True,
            'incl_lowercase': True,
            'incl_numbers':   True,
            'incl_symbols':   True
        }

    def _take_bool_input(self, prompt_txt):
        """Takes validated y/n boolean question response from user in terminal, 
            using the specified prompt appended with "(y/n): "

        Args:
            prompt_txt (str): The text to display at prompt

        Returns:
            Boolean or Nonetype: value of user input or None if failed to parse
        """
        val = input(prompt_txt + " (y/n): ")

        # Try to parse user input
        if (val == 'y') or (val == 'Y'):
            return True
        elif (val == 'n') or (val == 'N'):
            return False
        else:
            return None

    
    def collect_specs(self):
        """Collect all password generation parameters from user via console prompt"""
        
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
        """Generate n passwords based on passed parameters

        Args:
            count (int, optional): Number of passwords to generate. Defaults to 1.

        Returns:
            str list: List of generated password strings
        """
        passwords_out = []
        while count > 0:
            curr_pass = ""
            for _ in range(self.pass_length):
                
                # Choose a valid charset from which to pick a char
                keylist = list(self.flags)
                chosen_set = random.randint(0,3)
                while not self.flags[keylist[chosen_set]]:
                    chosen_set = random.randint(0,3)

                # Choose random char in charset and append to current gen password
                newchar = chr(random.randint(
                    CHAR_RANGES[chosen_set][0],
                    CHAR_RANGES[chosen_set][1],
                ))
                curr_pass = curr_pass + newchar

            passwords_out.append(curr_pass)
            count -= 1
        return passwords_out


if __name__ == '__main__':
    generator = PassGen()   # Init password generator class instance

    generator.collect_specs()   # Collect parameters for generation from user

    # Collect number of passwords to generate from user (not validated)
    num_to_gen =int(input("Number of passwords to generate: "))

    final_passwords = generator.generate(num_to_gen)    # Generate passwords

    print("\nGenerated Passwords:")
    [print(s) for s in final_passwords]

