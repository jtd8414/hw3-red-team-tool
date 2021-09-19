# -----------------------------------------------------------
# Key Distort: A program for altering user input to make typing useless.
#
# Joshua Dunn
# email jtd8414@rit.edu
# -----------------------------------------------------------

import keyboard
import string
import random


def on_key_press(event):
    """Event handler for key presses"""

    # delete previous character printed
    keyboard.write('\b')

    # generate a random character and print it to the screen.
    random_char = random.choice(string.ascii_letters)
    keyboard.write(random_char)


# Set-up event handler for key presses
keyboard.on_press(on_key_press)

# Block until user presses esc.
keyboard.wait('esc')
