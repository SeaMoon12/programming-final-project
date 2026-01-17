from termcolor import colored
import os
import sys

import main
import settings
import dialogues
import minigames
from settings import slow_print as print

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.all_locations = []
        for room in settings.room_config:
            if 'isHidden' not in settings.room_config[room]:
                self.all_locations.append(room)

        self.visited_locations = ['foyer']
        self.current_location = ''

        self.actions = ['continue', 'deep search']
        self.searching = False

        self.minigame = minigames.Minigames()
        self.minigame_result = False

        self.found_brochure = False
        self.found_gloves = False
        self.found_socks = False

        self.introduction()

# Introduction
    def introduction(self):
        os.system('cls')

        print(dialogues.newspaper)
        input('')
        self.rooms('foyer')

# FUNCTION FOR ROOMS
    def rooms(self, current_location):
        os.system('cls')
        self.current_location = current_location

        config = settings.room_config.get(current_location)

        intro = dialogues.rooms[current_location]['introduction']
        character = self.__class__.__name__.replace('Story', '').lower()
        print(character)
        success = dialogues.rooms[current_location]['success'][character]
        fail = dialogues.rooms[current_location]['fail']
        
        print(intro)
        input('')

        self.display_actions()

        if self.minigame_result:
            print(success)
            input()
            if config.get('isKeyRoom'):
                setattr(self, config['keyClue'], True)

            if 'unlocks' in config:
                self.all_locations.append(config['unlocks'])
                print(colored(f"New Location Unlocked: {config['unlocks'].capitalize()}\n",'green'))
        else:
            print(fail)
            input()

        self.display_rooms()

# == ACTIONS ==
    def search(self):
        config = settings.room_config[self.current_location]

        if config['searches'] > 0:
            self.searching = True
            config['searches'] -= 1
            print(config['searches'])
            print(dialogues.rooms[self.current_location]['minigame_intro'])
            input('')
            game_to_run = getattr(self.minigame, config['minigame'])
            self.minigame_result = game_to_run()
        else:
            print(colored('Sorry, you have no more searches available for this room.','red'))

# == BTS ==
# TECHNICALITIES
    def display_actions(self):
        print('    What would you like to do? ', end='')
        print(colored(f"Searches Remaining: {settings.room_config[self.current_location]['searches']}\n", 'yellow'))

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
        self.rooms(room)

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
        clues_found = self.found_brochure and self.found_gloves and self.found_socks

        while True:
            if clues_found:
                choice = input(dialogues.accuse['with lily']).lower()
            else:
                choice = input(dialogues.accuse['without lily']).lower()

            if choice == 'arthur' or choice == '1':
                print('Wrong choice!')
                self.replay()
            elif choice == 'elara' or choice == '2':
                print('Wrong choice!')
                self.replay()
            elif (choice == 'lily' or choice == '3') and clues_found:
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