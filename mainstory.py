from termcolor import colored
import os
import sys

import main
import settings
import dialogues
import minigames
from settings import type_writer_print as print

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.all_locations = ['foyer', 'study', 'bedroom', 'library', 'kitchen']
        self.visited_locations = ['foyer']
        self.current_location = ''

        self.searching = False

        self.actions = ['continue', 'deep search']
        self.can_search = False

        # SEARCH LIMITS
        self.foyer_searches = settings.foyer_searches
        self.study_searches = settings.study_searches
        self.bedroom_searches = settings.bedroom_searches
        self.kitchen_searches = settings.kitchen_searches
        self.library_searches = settings.library_searches
        self.nursery_searches = settings.nursery_searches

        # RESULTS FOR THE MINIGAME
        self.foyer_minigame_result = False
        self.study_minigame_result = False
        self.bedroom_minigame_result = False
        self.kitchen_minigame_result = False
        self.library_minigame_result = False
        self.nursery_minigame_result = False

        # Key Evidence - If player don't have 2, cannot accuse Lily.
        self.found_glove = False
        self.found_brochure = False

        self.introduction()

# Introduction
    def introduction(self):
        os.system('cls')

        print(dialogues.newspaper)
        input('')

# FUNCTION FOR ROOMS
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

        if minigame_result == True and (self.current_location != 'library' and self.current_location != 'study') and self.can_search:
            print(success_dialogue)
            input('')
        elif minigame_result == False and (self.current_location != 'library' and self.current_location != 'study') and self.can_search:
            print(fail_dialogue)

        # IF LIBRARY (for obtain key clue)
        if minigame_result == True and self.current_location == 'library':
            self.found_glove = True

            print(success_dialogue)
            input('')

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

# == ACTIONS ==
    def search(self):
        self.searching = True
        match self.current_location:
            case 'foyer':
                if self.foyer_searches > 0:
                    self.foyer_searches -= 1
                    print(dialogues.foyer['minigame_intro'])
                    input('')
                    self.foyer_minigame_result = minigames.Minigames().anagram()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False
            case 'study':
                if self.study_searches > 0:
                    self.study_searches -= 1
                    print(dialogues.study['minigame_intro'])
                    input('')
                    self.study_minigame_result = minigames.Minigames().numbrle()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False
            case 'bedroom':
                if self.bedroom_searches > 0:
                    self.bedroom_searches -= 1
                    print(dialogues.bedroom['minigame_intro'])
                    input('')
                    self.bedroom_minigame_result = minigames.Minigames().wordle()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False
            case 'library':
                if self.library_searches > 0:
                    self.library_searches -= 1
                    print(dialogues.library['minigame_intro'])
                    input('')
                    self.library_minigame_result = minigames.Minigames().hangman()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False
            case 'kitchen':
                if self.kitchen_searches > 0:
                    self.kitchen_searches -= 1
                    print(dialogues.kitchen['minigame_intro'])
                    input('')
                    self.kitchen_minigame_result = minigames.Minigames().riddles()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False
            case 'nursery':
                if self.nursery_searches > 0:
                    self.nursery_searches -= 1
                    print(dialogues.nursery['minigame_intro'])
                    input('')
                    self.nursery_minigame_result = minigames.Minigames().cryptic()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
                    self.can_search = False

# == BTS ==
# TECHNICALITIES
    def display_actions(self):
        print('    What would you like to do? ', end='')

        match self.current_location:
            case 'foyer': print(colored(f'Searches Remaining: {self.foyer_searches}\n', 'yellow'))
            case 'study': print(colored(f'Searches Remaining: {self.study_searches}\n', 'yellow'))
            case 'bedroom': print(colored(f'Searches Remaining: {self.bedroom_searches}\n', 'yellow'))
            case 'kitchen': print(colored(f'Searches Remaining: {self.kitchen_searches}\n', 'yellow'))
            case 'library': print(colored(f'Searches Remaining: {self.library_searches}\n', 'yellow'))
            case 'nursery': print(colored(f'Searches Remaining: {self.nursery_searches}\n', 'yellow'))

        # Print actions
        for actions in self.actions:
            print(f'        {self.actions.index(actions)+1}. {actions.capitalize()}')

        while True:
            act_choice = input('\033[94m').lower() # \033[94m is bright blue
            print('\033[0m', end='') # \033[0m is reset

            for i in range(len(self.actions)):
                if act_choice == str(i+1):
                    act_choice = self.actions[i]

            if act_choice in self.actions:
                self.act(act_choice)
                break
            else:
                print(colored(f'That is not an available action. Please choose another action.', 'red'))

    def act(self, act):
        match act:
            case 'deep search': self.search()
            case 'continue': self.display_rooms()

    def display_rooms(self):
        loc_wo_cur = self.all_locations.copy()
        loc_wo_cur.remove(self.current_location)
        can_accuse = False
        has_not_visited = None
        has_visited = None

        # Check wheether player can accuse
        for room in self.all_locations:
            if room not in self.visited_locations:
                has_not_visited = True
            else:
                has_visited = True
        if has_not_visited:
            can_accuse = False
        else:
            can_accuse = True

        if can_accuse == True:
            print(colored('''\nYou have visited all rooms. You can now accuse the killer.\n''', 'green'))

        print('''    Where would you like to investigate next?
        ''')

        # Print locations
        for location in loc_wo_cur:
            print(f'        {loc_wo_cur.index(location)+1}. {location.capitalize()}')
        
        # Also print option to accuse if can accuse
        if can_accuse == True:
            print(f'        {len(loc_wo_cur)+1}. Accuse')

        while True:
            # Ask user for input
            room = input('\033[94m').lower()
            print('\033[0m', end='')

            # Handled number inputs - Change number to room name
            for i in range(len(loc_wo_cur)):
                if room == str(i+1):
                    room = loc_wo_cur[i]
            
            # location visit conditionals
            if room in loc_wo_cur:
                print(f'Entering {room}')
                if room not in self.visited_locations:
                    self.visited_locations.append(room)
                self.enter_room(room)
            elif room == self.current_location:
                print(colored(f'You are already in the {self.current_location.capitalize()}.', 'yellow'))

            # if user pick to accuse
            elif (room == 'accuse' or room == str(len(self.all_locations))) and (can_accuse == True):
                self.accuse_confirmation()

            # for debugging purposes
            elif room == 'visits':
                print(self.visited_locations)
            elif room == 'locations':
                print(self.all_locations)
            elif room == 'visit all':
                print('You have visited all locations.')
                self.visited_locations = self.all_locations
            elif room == 'display number of rooms':
                print(len(self.all_locations))

            else:
                print(colored('That room does not exist to your knowledge. Please choose another room.','red'))

    def enter_room(self, room):
        # different per character
        pass

# ACCUSATIONS
    def accuse_confirmation(self):
        choice = ''
        os.system('cls')
        while choice != 'y' or 'n':
            choice = input('Would you like to accuse now? (y/n)\n')
            if choice == 'y':
                self.accuse()
            elif choice == 'n':
                self.visited_locations = []
                print('Okay. Please visit all rooms again if you want to accuse.\n')
                self.display_rooms()
            else:
                print(colored('Invalid input. Please answer with \'y\' or \'n\'.', 'red'))

    def accuse(self):
        while True:
            if self.found_glove and self.found_brochure:
                choice = input(dialogues.accuse['with lily']).lower()
            else:
                choice = input(dialogues.accuse['without lily']).lower()

            if choice == 'arthur' or choice == '1':
                print('Wrong choice!')
                self.replay()
            elif choice == 'elara' or choice == '2':
                print('Wrong choice!')
                self.replay()
            elif (choice == 'lily' or choice == '3') and self.found_brochure and self.found_glove:
                print('Congratulations, you picked the right killer.')
                self.replay()
            else:
                print('Invalid Choice. Please enter according to the options provided.')
                continue

    def replay(self):
        choice = input('Would you like to try again? (y/n)\n')
        if choice == 'y' or choice == 'yes':
            main.Main()
        else:
            sys.exit()