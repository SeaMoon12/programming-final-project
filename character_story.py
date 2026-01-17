from termcolor import colored
import os

import settings
import mainstory
import dialogues
import minigames
from settings import type_writer_print as print

# If there are events that may happen, this class will allow these events to happen based on the character chosen
class StoryParanormal(mainstory.Story):
    pass

class StoryPrivateInvestigator(mainstory.Story):
    def __init__(self):
        self.special_use = settings.investigator_searches
        super().__init__()

    def display_rooms(self):
        while True:
            if self.special_use > 0 and self.searching and self.minigame_result:
                self.minigame_result = False

                choice = input(f'''Use Authority Check? (Remaining: {self.special_use}) (y/n)''').lower()
                if choice == 'y' or choice == 'yes':
                    self.special_use -= 1
                    print(dialogues.rooms[self.current_location]['success']['investigator_special'])
                    input('')
                    break
                    self.searching = False
                elif choice == 'n' or choice == 'no':
                    self.searching = False
                    break
                else:
                    print(colored('\nPlease answer with \'yes\' or \'no\'.\n','red'))
                    continue
            else:
                break
                    
        super().display_rooms()

class StoryBuyer(mainstory.Story):
    pass