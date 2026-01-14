from termcolor import colored
import os

import minigames

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.all_locations = ['foyer', 'study', 'bedroom', 'library', 'kitchen']
        self.visited_locations = ['foyer']
        self.current_location = ''
        self.items = []

        self.introduction()
        
    def introduction(self):
        os.system('cls')

        print('''
    THE BLACKWOOD GAZETTE
    Vol. LXVIII — No. 242 | Tuesday, October 14, 2010 | Price: £1.50

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
                weapon—believed to be a silver letter opener  from the  Lord’s
                own  desk—remains  missing.  Detective  Inspector  Graves  has
                characterized the slaying as a "crime of passion," citing  the
                intimate nature of the attack.

            The Inner Circle Under Fire
                As the investigation unfolds, the movements of  those  closest
                to the Lord have come under intense scrutiny:

                    - Arthur Blackwood (Son): The  heir  apparent  provided  a
                      confirmed alibi at the Royal  Casino. However, witnesses
                      noted Arthur stepped out for "an hour  of air"  at  3:00
                      AM—the estimated time of the struggle.

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
                battle over the estate—a shadow that will loom over the  manor
                until a new owner dares to claim it.

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
        As you stand before the giant door, you thought why nobody wanted this place. Walking into
        the room, you find two objects that immediately stand out before the rest:
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
    LOCATION: The Private Study
        Walking into the study, you see a half-full brandy glass smelling of Bitter Almonds (Arsenic)
        and a shredded Will that would have left Arthur with absolutely nothing. Rummaging through
        the drawers of the desk, you found a black box which appears to be a Safe.

    PRESS ENTER TO CONTINUE''')
        input('')

# BEDROOM
    def bedroom(self):
        os.system('cls')
        self.current_location = 'bedroom'

        print('''
    LOCATION: The Master Bedroom
        Upon entering the bedroom, you see a packed suitcase and a one-way ticket to Paris on the floor,
        beside the bed. On the bed, you see a blackmail letter from Arthur to Elara about her secret lover.
        Across from the packed suitcase, on the other side of the bed, is something small... Something red...
        As you move closer, you find...

    PRESS ENTER TO CONTINUE''')
        input('')

        minigames.Minigames().wordle()

        print('''
        A Bloody Letter Opener

    PRESS ENTER TO CONTINUE''')
        input('')

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
        Stepping into the library, you browse through all the books available when you stumble upon a photo.
        It turns out that Elara had a secret lover: The Lawyer. Her husband had not known anything about this.
        After going through several book isles, you found a marriage contract between Alistair and his wife.
        It says that if Elara ever had a divorce with him, Elara would lose everything. While sitting on the
        couch, you saw something in the corner of your eye.

    PRESS ENTER TO CONTINUE''')
        input('')

        minigames.Minigames().hangman()

    # NURSERY
    def nursery(self):
        os.system('cls')
        self.current_location = 'nursery'

        print('''
    LOCATION: The Nursery

        Which room do you want to investigate?
        ''')

# TECHNICALITIES
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
        can_accuse = False
        choice = ''

        for location in self.all_locations:
            if location not in self.visited_locations:
                can_accuse = False
                break
            else:
                can_accuse = True
        if can_accuse == True:
            os.system('cls')
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