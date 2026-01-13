import minigames

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
    Newspaper from 2010
        
        The Victim: Lord Alistair Blackwood (72).
        The Discovery: Found by the Maid at 6:00 AM in his locked Study.
        Police Assumption: A "Crime of Passion." Alistair was stabbed once in the neck with a letter opener (later found to be missing).
        The Suspects' Alibis:
            - Arthur (Son): Claims he was at the local casino (witnesses confirmed he was there, but he left for an "hour of air" at 3:00 AM).
            - Elara (Wife): Claims she was asleep in her room. No witnesses.
            - Lily (Granddaughter): Only 10 at the time; police ruled her out immediately as "physically incapable."
        The Conclusion: Case closed due to "Lack of Evidence." The estate was tied up in legal battles until you bought it.

    PRESS ENTER TO CONTINUE
        ''')
        input('')
        self.foyer()

# FOYER
    def foyer(self):
        os.system('cls')
        self.current_location = 'foyer'

        print('''
    LOCATION: The Grand Foyer
        As you stand before the giant door, you thought why nobody wanted this place. Walking into the room, you find two objects that immediately stand out before the rest:
            1. A rusted walking cane with a heavy gold top that belonged to Arthur
            2. An 8-year-old eviction notice Alistair wrote addressed to Arthur
        But you notice something... something that stands out more than the two objects...

    PRESS ENTER TO CONTINUE''')
        input('')

        minigames.Minigames().anagram()

# STUDY
    def study(self):
        os.system('cls')
        self.current_location = 'study'

        print('''
    LOCATION: The Study
        ...
        ''')

# BEDROOM
    def bedroom(self):
        os.system('cls')
        self.current_location = 'bedroom'

        print('''
    LOCATION: The Master Bedroom
        ...

        Which room do you want to investigate?
        ''')

# KITCHEN
    def kitchen(self):
        os.system('cls')
        self.current_location = 'kitchen'

        print('''
    LOCATION: The Kitchen

        Which room do you want to investigate?
        ''')

# LIBRARY
    def library(self):
        os.system('cls')
        self.current_location = 'library'

        print('''
    LOCATION: The Library

        Which room do you want to investigate?
        ''')

# NURSERY
    def nursery(self):
        os.system('cls')
        self.current_location = 'nursery'

        print('''
    LOCATION: The Nursery

        Which room do you want to investigate?
        ''')

    def path(self):
        loc_wo_cur = self.all_locations.copy()
        loc_wo_cur.remove(self.current_location)

        print('''    Where would you like to investigate next?
        ''')

        # Print locations
        for location in loc_wo_cur:
            print(f'        {loc_wo_cur.index(location)+1}. {location.capitalize()}')

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