import random
import sys
import time
from termcolor import colored

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

    def anagram(self):
        print('''        Turn these letters to make new existing word: A-S-T-U-T-E-R.
        You only have 5 chances to guess the word, if you  fail  you  won't  be
        able to obtain the clue.Think wisely before answering, the fate  is  in
        your hand
        ''')

        answer= input("Write your answer: ").lower()

        for chances in range(4):
            if answer == "stature":
                print('CORRECT')
                return True
            elif answer != "stature":
                answer = input(colored('The answer is still incorrect, try again:\n','red'))
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
