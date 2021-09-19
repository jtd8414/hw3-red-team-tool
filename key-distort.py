import keyboard
import string
import random


def on_key_press(event):
    # delete previous character printed
    keyboard.write('\b')

    # generate a random character and print it to the screen.
    random_char = random.choice(string.ascii_letters)
    keyboard.write(random_char)


keyboard.on_press(on_key_press)

# Blocks until you press esc.
keyboard.wait('esc')
