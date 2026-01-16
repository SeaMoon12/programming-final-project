from termcolor import colored
import os
import sys
import time

import settings
import mainstory
import dialogues
import minigames

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

# If there are events that may happen, this class will allow these events to happen based on the character chosen
class StoryParanormal(mainstory.Story):
    def __init__(self):
        self.role = 'paranormal'
        super().__init__()

    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print(dialogues.foyer['success']['paranormal'])
            input('')
        elif self.foyer_minigame_result == False:
            print(dialogues.foyer['fail'])
            input('')
        
        self.foyer_minigame_result = None
        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            self.found_brochure = True
            print(dialogues.study['success']['paranormal'])
            input('')
        elif self.study_minigame_result == False:
            print(dialogues.study['fail'])
            input('')

        self.study_minigame_result = None
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print(dialogues.bedroom['success']['paranormal'])
            input('')
        elif self.bedroom_minigame_result == False:
            print(dialogues.bedroom['fail'])
            input('')

        self.bedroom_minigame_result = None
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print(dialogues.kitchen['success']['paranormal'])
            input('')
        elif self.kitchen_minigame_result == False:
            print(dialogues.kitchen['fail'])
            input('')

        self.kitchen_minigame_result = None
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()
        
        if self.library_minigame_result == True:
            self.found_glove = True

            print(dialogues.library['success']['paranormal'])
            input('')
        elif self.library_minigame_result == False:
            print(dialogues.library['fail'])
            input('')

        self.library_minigame_result = None
        self.display_rooms()

class StoryPrivateInvestigator(mainstory.Story):
    def __init__(self):
        self.special_use = settings.investigator_searches
        self.role = 'investigator'
        super().__init__()

    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print(dialogues.foyer['success']['investigator'])
            input('')
        elif self.foyer_minigame_result == False:
            print(dialogues.foyer['fail'])
            input('')

        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            self.found_brochure = True
            print(dialogues.study['success']['investigator'])
            input('')
        elif self.study_minigame_result == False:
            print(dialogues.study['fail'])
            input('')

        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print(dialogues.bedroom['success']['investigator'])
            input('')
        elif self.bedroom_minigame_result == False:
            print(dialogues.bedroom['fail'])
            input('')

        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print(dialogues.kitchen['success']['investigator'])
            input('')
        elif self.kitchen_minigame_result == False:
            print(dialogues.kitchen['fail'])
            input('')

        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        if self.library_minigame_result == True:
            self.found_glove = True
            print(dialogues.library['success']['investigator'])
            input('')
        elif self.library_minigame_result == False:
            print(dialogues.library['fail'])
            input('')

        self.display_rooms()

    def display_rooms(self):
        minigame_result = self.foyer_minigame_result or self.study_minigame_result or self.bedroom_minigame_result or self.kitchen_minigame_result or self.library_minigame_result
        while True:
            if self.special_use > 0 and self.searching and minigame_result:
                self.foyer_minigame_result = False
                self.study_minigame_result = False
                self.bedroom_minigame_result = False
                self.kitchen_minigame_result = False
                self.library_minigame_result = False

                self.searching = False
                choice = input(f'''Use Authority Check? (Remaining: {self.special_use})''').lower()
                if choice == 'y' or choice == 'yes':
                    self.special_use -= 1
                    match self.current_location:
                        # FOYER
                        case 'foyer':
                            print(dialogues.foyer['investigator_special'])
                            input('')
                            break

                        # STUDY
                        case 'study':
                            print(dialogues.study['success']['investigator_special'])
                            input('')
                            break

                        # BEDROOM
                        case 'bedroom':
                            print(dialogues.bedroom['success']['investigator_special'])

                        # KITCHEN
                        case 'kitchen':
                            print(dialogues.kitchen['success']['investigator_special'])

                        # LIBRARY
                        case 'library':
                            print(dialogues.library['success']['investigator_special'])
                            input('')
                            break
                elif choice == 'n' or choice == 'no':
                    break
                else:
                    print('Please answer with \'yes\' or \'no\'.')
            else:
                break
                    
        super().display_rooms()

class StoryBuyer(mainstory.Story):
    def __init__(self):
        self.role = 'buyer'
        super().__init__()

    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print(dialogues.foyer['success']['buyer'])
            input('')
        elif self.foyer_minigame_result == False:
            print(dialogues.foyer['fail'])
            input('')

        self.foyer_minigame_result = None
        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            self.found_brochure = True
            print(dialogues.study['success']['buyer'])
            input('')
        elif self.study_minigame_result == False:
            print(dialogues.study['fail'])
            input('')

        self.study_minigame_result = None
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print(dialogues.bedroom['success']['buyer'])
            input('')
        elif self.bedroom_minigame_result == False:
            print(dialogues.bedroom['fail'])
            input('')

        self.bedroom_minigame_result = None
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print(dialogues.kitchen['success']['buyer'])
            input('')
        elif self.kitchen_minigame_result == False:
            print(dialogues.kitchen['fail'])
            input('')

        self.kitchen_minigame_result = None
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        if self.library_minigame_result == True:
            self.found_glove = True

            print(dialogues.library['success']['buyer'])
            input('')

            self.all_locations.append('nursery')

            print(colored('You now have access to the Nursery\n', 'green'))

        elif self.library_minigame_result == False:
            print(dialogues.library['fail'])
            input('')

        self.library_minigame_result = None
        self.display_rooms()

    # NURSERY
    def nursery(self):
        super().nursery()

        if self.nursery_minigame_result == True:
            print(dialogues.nursery['success'])
            input('')
        elif self.nursery_minigame_result == False:
            print(dialogues.nursery['fail'])
            input('')

        self.nursery_minigame_result = None
        self.display_rooms()
