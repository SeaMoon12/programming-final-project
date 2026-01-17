from termcolor import colored
import os

import settings
import character_story
from settings import type_writer_print as print

class Main:
    def __init__(self):
        self.character_selection()

    def character_selection(self):
        while True:
            os.system('cls')
            print('''
    Who do you want to play as?
        1. The Paranormal
            Difficulty      : Easy
            Unique Ability  : Spirit Whisperer
            Receives cryptic, fragmented messages from Alistair's ghost

        2. The Private Investigator
            Difficulty      : Medium
            Unique Ability  : Authority Check
            Able to check the truth of one clue (can only be used once)

        3. The Buyer
            Difficulty      : Hard
            Unique Ability  : Blueprint Access
            Can find secret passages and evaluate the layout of the manor
''')
            char_choice = input('').lower()
            if char_choice == 'paranormal' or char_choice ==  'the paranormal' or char_choice ==  '1':
                self.story = character_story.StoryParanormal()
                break
            elif char_choice == 'investigator' or char_choice == 'the investigator' or char_choice == '2' or char_choice == 'the private investigator' or char_choice == 'private investigator':
                self.story = character_story.StoryPrivateInvestigator()
                break
            elif char_choice == 'buyer' or char_choice == 'the buyer' or char_choice == '3':
                self.story = character_story.StoryBuyer()
                break
            else:
                os.system('cls')
                print(colored('Invalid character. Please try again.', 'red'))


if __name__ == "__main__":
    app = Main()