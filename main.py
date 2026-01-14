from termcolor import colored
import os

import character_story

class Main:
    def __init__(self):
        self.character_selection()

    def character_selection(self):
        while True:
            char_choice = input('''
    Who do you want to play as?
        1. The Paranormal
            Difficulty      : Easy
            Unique Ability  : Spirit Whisperer
            Receives cryptic, fragmented messages from Alistair's ghost

        2. The Private Investigator
            Difficulty      : Medium
            Unique Ability  : Authority Check?
            ???

        3. The Buyer
            Difficulty      : Hard
            Unique Ability  : Blueprint Access
            Can find secret passages and evaluate the layout of the manor
''').lower()
            if char_choice == 'paranormal' or char_choice ==  'the paranormal' or char_choice ==  '1':
                self.story = character_story.StoryParanormal()
                break
            elif char_choice == 'investigator' or char_choice == 'the investigator' or char_choice == '2' or char_choice == 'the private investigator':
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