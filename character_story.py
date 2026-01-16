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

    def enter_room(self, room):
        match room:
            case 'foyer': self.rooms('foyer', dialogues.foyer['introduction'], dialogues.foyer['success']['paranormal'], dialogues.foyer['fail'])
            case 'study': self.rooms('study', dialogues.study['introduction'], dialogues.study['success']['paranormal'], dialogues.study['fail'])
            case 'bedroom': self.rooms('bedroom', dialogues.bedroom['introduction'], dialogues.bedroom['success']['paranormal'], dialogues.bedroom['fail'])
            case 'kitchen': self.rooms('kitchen', dialogues.kitchen['introduction'], dialogues.kitchen['success']['paranormal'], dialogues.kitchen['fail'])
            case 'library': self.rooms('library', dialogues.library['introduction'], dialogues.library['success']['paranormal'], dialogues.library['fail'])
            case 'nursery': self.rooms('nursery', dialogues.nursery['introduction'], dialogues.nursery['success']['paranormal'], dialogues.nursery['fail'])

class StoryPrivateInvestigator(mainstory.Story):
    def __init__(self):
        self.special_use = settings.investigator_searches
        self.role = 'investigator'
        super().__init__()

    def enter_room(self, room):
        match room:
            case 'foyer': self.rooms('foyer', dialogues.foyer['introduction'], dialogues.foyer['success']['investigator'], dialogues.foyer['fail'])
            case 'study': self.rooms('study', dialogues.study['introduction'], dialogues.study['success']['investigator'], dialogues.study['fail'])
            case 'bedroom': self.rooms('bedroom', dialogues.bedroom['introduction'], dialogues.bedroom['success']['investigator'], dialogues.bedroom['fail'])
            case 'kitchen': self.rooms('kitchen', dialogues.kitchen['introduction'], dialogues.kitchen['success']['investigator'], dialogues.kitchen['fail'])
            case 'library': self.rooms('library', dialogues.library['introduction'], dialogues.library['success']['investigator'], dialogues.library['fail'])
            case 'nursery': self.rooms('nursery', dialogues.nursery['introduction'], dialogues.nursery['success']['investigator'], dialogues.nursery['fail'])

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

    def enter_room(self, room):
        match room:
            case 'foyer': self.rooms('foyer', dialogues.foyer['introduction'], dialogues.foyer['success']['buyer'], dialogues.foyer['fail'])
            case 'study': self.rooms('study', dialogues.study['introduction'], dialogues.study['success']['buyer'], dialogues.study['fail'])
            case 'bedroom': self.rooms('bedroom', dialogues.bedroom['introduction'], dialogues.bedroom['success']['buyer'], dialogues.bedroom['fail'])
            case 'kitchen': self.rooms('kitchen', dialogues.kitchen['introduction'], dialogues.kitchen['success']['buyer'], dialogues.kitchen['fail'])
            case 'library': self.rooms('library', dialogues.library['introduction'], dialogues.library['success']['buyer'], dialogues.library['fail'])
            case 'nursery': self.rooms('nursery', dialogues.nursery['introduction'], dialogues.nursery['success'], dialogues.nursery['fail'])

    def rooms(self, current_location, introduction_dialogue, success_dialogue, fail_dialogue):
        os.system('cls')
        self.current_location = current_location
        
        print(introduction_dialogue)
        input('')

        self.display_actions()

        match current_location:
            case 'foyer': minigame_result = self.foyer_minigame_result
            case 'study': minigame_result = self.study_minigame_result
            case 'bedroom': minigame_result = self.bedroom_minigame_result
            case 'kitchen': minigame_result = self.kitchen_minigame_result
            case 'library': minigame_result = self.library_minigame_result
            case 'nursery': minigame_result = self.nursery_minigame_result

        if minigame_result == True and (self.current_location != 'library' and self.current_location != 'study'):
            print(success_dialogue)
            input('')
        elif minigame_result == False and (self.current_location != 'library' and self.current_location != 'study'):
            print(fail_dialogue)

        # IF LIBRARY (for obtain key clue)
        if minigame_result == True and self.current_location == 'library':
            self.found_glove = True

            print(success_dialogue)
            input('')

            self.all_locations.append('nursery')
            print(colored('You now have access to the Nursery\n', 'green'))

        elif minigame_result == False and self.current_location == 'library':
            print(fail_dialogue)
            input('')

        # IF STUDY (for obtain key clue)
        if minigame_result == True and self.current_location == 'study':
            self.found_brochure = True

            print(success_dialogue)
            input('')

        elif minigame_result == False and self.current_location == 'study':
            print(fail_dialogue)
            input('')

        minigame_result = None
        self.display_rooms()