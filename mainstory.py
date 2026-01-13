from termcolor import colored
import os

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.all_locations = ['foyer', 'study', 'bedroom', 'kitchen', 'library']
        self.visited_locations = ['foyer']
        self.current_location = ''
        self.items = []

        self.introduction()
        
    def introduction(self):
        os.system('cls')

        print('''
        Setting: Blackwood Manor, the night after Lord Alistair Blackwood is found dead in a locked study.
        The Conflict: Alistair was hours away from disinheriting his family to fund an orphanage.
        The Objective: Identify the killer before the police arrive.

        PRESS ENTER TO CONTINUE
        ''')
        input('')
        self.foyer()

    def foyer(self):
        # What needs to be done at the start
        os.system('cls')
        self.current_location = 'foyer'

        print('''
    LOCATION: The Grand Foyer
        In front of you lies The Will: A document on the table stating the estate goes to "The St. Jude Orphanage"
        tomorrow and The Argument Log: A servant’s diary noting a "violent shouting match" between Alistair and Arthur.

        Which room do you want to investigate?
        ''')
        self.path() # We will not include this line in this file, but in the character_story.py file

    def study(self):
        os.system('cls')
        self.current_location = 'study'

        self.path()

    def bedroom(self):
        os.system('cls')
        self.current_location = 'bedroom'

        self.path()

    def kitchen(self):
        os.system('cls')
        self.current_location = 'kitchen'

        self.path()

    def library(self):
        os.system('cls')
        self.current_location = 'library'

        self.path()

    def nursery(self):
        os.system('cls')
        self.current_location = 'nursery'

        self.path()

    def path(self):
        loc_wo_cur = self.all_locations.copy()
        loc_wo_cur.remove(self.current_location)

        # Print locations
        for location in loc_wo_cur:
            print(f'{loc_wo_cur.index(location)+1}. {location.capitalize()}')

        while True:
            room = input('').lower()

            # Handled number inputs - Change number to room name
            for i in range(len(loc_wo_cur)):
                if room == str(i+1):
                    room = loc_wo_cur[i]
            
            if room in loc_wo_cur:
                print(f'Entered {room}')
                if room not in self.visited_locations:
                    self.visited_locations.append(room)
                self.enter_room(room)
            elif room == self.current_location:
                print(f'You are already in the {self.current_location.capitalize()}.')
            else:
                print(colored('Invalid room. Please try again.','red'))

    def enter_room(self, room):
        match room:
            case 'foyer': self.foyer()
            case 'study': self.study()
            case 'bedroom': self.bedroom()
            case 'kitchen': self.kitchen()
            case 'library': self.library()
            case 'nursery': self.nursery()

    def accuse(self):
        os.system('cls')
        can_accuse = False
        choice = ''

        for location in self.all_locations:
            if location not in self.visited_locations:
                can_accuse = False
                break
            else:
                can_accuse = True
        if can_accuse == True:
            while choice != 'y' or 'n':
                choice = input('Would you like to accuse now? (y/n)')
                if choice == 'y':
                    pass
                    # accuse
                elif choice == 'n':
                    can_accuse = False
                    self.visited_locations = []
                    print('Okay. Please visit all rooms again if you want to accuse.')
                    break
                else:
                    print(colored('Invalid input. Please answer with \'y\' or \'n\'.', 'red'))