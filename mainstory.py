from termcolor import colored
import os
import sys
import time

import main
import settings
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

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.role = None

        self.all_locations = ['foyer', 'study', 'bedroom', 'library', 'kitchen']
        self.visited_locations = ['foyer']
        self.current_location = ''

        self.searching = False

        self.actions = ['continue', 'deep search']

        # SEARCH LIMITS
        self.foyer_searches = settings.foyer_searches
        self.study_searches = settings.study_searches
        self.bedroom_searches = settings.bedroom_searches
        self.kitchen_searches = settings.kitchen_searches
        self.library_searches = settings.library_searches
        self.nursery_searches = settings.nursery_searches

        # RESULTS FOR THE MINIGAME
        self.foyer_minigame_result = None
        self.study_minigame_result = None
        self.bedroom_minigame_result = None
        self.kitchen_minigame_result = None
        self.library_minigame_result = None
        self.nursery_minigame_result = None

        # Key Evidence - If player don't have 2, cannot accuse Lily.
        self.found_glove = False
        self.found_brochure = False

        self.introduction()

# Introduction
    def introduction(self):
        os.system('cls')

        print('''
    THE BLACKWOOD GAZETTE
    Vol. LXVIII - No. 242 | Tuesday, October 14, 2010 | Price: £1.50

        ======== TRAGEDY AT BLACKWOOD MANOR: LORD ALISTAIR FOUND DEAD ========
          POLICE PROBE "CRIME OF PASSION" IN LOCKED-ROOM MYSTERY
          By Julian Vane, Investigative Reporter
        
            BLACKWOOD ESTATE –  The  prestigious  Blackwood  family  has  been
            thrust  into   a   "living   nightmare"  following   the  gruesome
            discovery of Lord Alistair Blackwood (72)  early  Monday  morning.
            The patriarch, a man known for his iron-fisted  control  over  the
            local shipping industry, was found deceased in his  private  study
            at approximately 6:00 AM.

            A Gruesome Discovery
                The body was discovered by  the  estate’s  long-serving  maid,
                Martha Higgins, when she arrived to deliver the Lord’s morning
                tea. According to police reports, the study  door  was  locked
                from the  inside.  Investigators  state  that  Lord  Blackwood
                succumbed to a single, fatal puncture wound to  the  neck. The
                weapon-believed to be a silver letter opener  from the  Lord’s
                own  desk-remains  missing.  Detective  Inspector  Graves  has
                characterized the slaying as a "crime of passion," citing  the
                intimate nature of the attack.

            The Inner Circle Under Fire
                As the investigation unfolds, the movements of  those  closest
                to the Lord have come under intense scrutiny:

                    - Arthur Blackwood (Son): The  heir  apparent  provided  a
                      confirmed alibi at the Royal  Casino. However, witnesses
                      noted Arthur stepped out for "an hour  of air"  at  3:00
                      AM-the estimated time of the struggle.

                    - Lady Elara Blackwood (Wife): Lady  Elara  maintains  she
                      was asleep in her separate wing of the  manor.  With  no
                      witnesses to  verify  her  whereabouts,  she  remains  a
                      person of interest.

                    - Lily  Blackwood  (Granddaughter):  The  10-year-old  was
                      present in the house, but  authorities  have  officially
                      ruled her out. "A child of  her  stature  is  physically
                      incapable of such a calculated  strike,"  Graves  noted.
            
            CASE CLOSED: NO JUSTICE FOR ALISTAIR
                [UPDATE: Nov 12, 2010] In a shocking turn of events, the Crown
                Prosecution  Service  has  announced  the  suspension  of  the
                Blackwood investigation. Despite the missing  weapon  and  the
                gaps in the family's alibis, officials cited a "total lack  of
                forensic evidence" to move forward. The Blackwood fortune  now
                hangs in limbo, as the family prepares  for  a  lengthy  legal
                battle over the estate-a shadow that will loom over the  manor
                until a new owner dares to claim it.

    PRESS ENTER TO CONTINUE
        ''')
        input('')
        self.foyer()

# == ROOMS ==
# FOYER
    def foyer(self):
        os.system('cls')
        self.current_location = 'foyer'

        print(dialogues.foyer['introduction'])
        input('')

        self.display_actions()

# STUDY
    def study(self):
        os.system('cls')
        self.current_location = 'study'

        print(dialogues.study['introduction'])
        input('')

        self.display_actions()

# BEDROOM
    def bedroom(self):
        os.system('cls')
        self.current_location = 'bedroom'

        print(dialogues.bedroom['introduction'])
        input('')

        self.display_actions()

# KITCHEN
    def kitchen(self):
        os.system('cls')
        self.current_location = 'kitchen'

        print(dialogues.kitchen['introduction'])
        input('')

        self.display_actions()

# LIBRARY
    def library(self):
        os.system('cls')
        self.current_location = 'library'

        print(dialogues.library['introduction'])
        input('')

        self.display_actions()

    # NURSERY
    def nursery(self):
        os.system('cls')
        self.current_location = 'nursery'

        print(dialogues.nursery['introduction'])

        self.display_actions()

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
            case 'study':
                if self.study_searches > 0:
                    self.study_searches -= 1
                    print(dialogues.study['minigame_intro'])
                    input('')
                    self.study_minigame_result = minigames.Minigames().numbrle()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
            case 'bedroom':
                if self.bedroom_searches > 0:
                    self.bedroom_searches -= 1
                    print(dialogues.bedroom['minigame_intro'])
                    input('')
                    self.bedroom_minigame_result = minigames.Minigames().wordle()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
            case 'library':
                if self.library_searches > 0:
                    self.library_searches -= 1
                    print(dialogues.library['minigame_intro'])
                    input('')
                    self.library_minigame_result = minigames.Minigames().hangman()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
            case 'kitchen':
                if self.kitchen_searches > 0:
                    self.kitchen_searches -= 1
                    print(dialogues.kitchen['minigame_intro'])
                    input('')
                    self.kitchen_minigame_result = minigames.Minigames().riddles()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))
            case 'nursery':
                if self.nursery_searches > 0:
                    self.nursery_searches -= 1
                    print(settings.nursery_dialogue)
                    input('')
                    self.nursery_minigame_result = minigames.Minigames().cryptic()
                else:
                    print(colored('Sorry, you have no more searches available for this room.','red'))

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
            elif room == 'show evidence':
                print(self.key_evidence)

            else:
                print(colored('That room does not exist to your knowledge. Please choose another room.','red'))

    def enter_room(self, room):
        match room:
            case 'foyer': self.foyer()
            case 'study': self.study()
            case 'bedroom': self.bedroom()
            case 'kitchen': self.kitchen()
            case 'library': self.library()
            case 'nursery': self.nursery()

# ACCUSATIONS
    def accuse_confirmation(self):
        choice = ''
        os.system('cls')
        while choice != 'y' or 'n':
            choice = input('Would you like to accuse now? (y/n)\n')
            if choice == 'y':
                print('Accusing')
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
                choice = input('''
        Who would you like to accuse?

            1. Arthur
            2. Elara
            3. Lily
                
        ''').lower()
            else:
                choice = input('''
        Who would you like to accuse?

            1. Arthur
            2. Elara
                
        ''').lower()

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
        choice = input('Would you like to try again?')
        if choice == 'y' or choice == 'yes':
            main.Main()
        else:
            sys.exit()