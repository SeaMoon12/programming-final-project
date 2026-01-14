import random
import sys
import time

import settings

def print(*args, **kwargs):
    # Extract speed settings if provided, otherwise use defaults
    speed = kwargs.pop('speed', settings.print_speed)
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    
    # Combine all arguments into one string (mimicking standard print)
    message = sep.join(map(str, args))
    
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    
    # Print the ending (usually a newline)
    sys.stdout.write(end)
    sys.stdout.flush()

class Minigames:
    def __init__(self):
        pass
    def hangman(self):
        print('running game hangman')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def wordle(self):
        print('running game wordle')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def numbrle(self):
        print('running game numbrle')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def scramble(self):
        print('running game scramble')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def anagram(self):
        print('running game anagram')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def cryptic(self):
        print('running game cryptic')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False
            
    def riddles(self):
        print('running game riddles')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False
