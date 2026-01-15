from termcolor import colored
import os
import sys
import time

import settings
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
        self.all_locations = ['foyer', 'study', 'bedroom', 'library', 'kitchen']
        self.visited_locations = ['foyer']
        self.current_location = ''

        self.actions = ['continue', 'deep search']

        # RESULTS FOR THE MINIGAME
        self.foyer_minigame_result = None
        self.study_minigame_result = None
        self.bedroom_minigame_result = None
        self.kitchen_minigame_result = None
        self.library_minigame_result = None
        self.nursery_minigame_result = None

        self.introduction()

# Introduction
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

# == ROOMS ==
# FOYER
    def foyer(self):
        os.system('cls')
        self.current_location = 'foyer'

        print('''
    LOCATION: The Grand Foyer
        The heavy oak doors seal behind you with a thud that vibrates in  your
        marrow. To your left, a heap of discarded yellow  envelopes  addressed
        to Arthur spills from a rusted mail slot—stamped with the red  ink  of
        "Final Notice." A shattered porcelain vase lies across the  floor, its
        shards like jagged teeth.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_actions()

# STUDY
    def study(self):
        os.system('cls')
        self.current_location = 'study'

        print('''
    LOCATION: The Private Study
        Two porcelain teacups sit on the desk, the residue smelling of  bitter
        almonds. A shredded Will lies in a heap of confetti.  The  high-backed
        chair sits facing away from the door, towards the wall.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_actions()

# BEDROOM
    def bedroom(self):
        os.system('cls')
        self.current_location = 'bedroom'

        print('''
    LOCATION: The Master Bedroom
        Moth-eaten curtains hang like flayed skin. A half-packed suitcase sits
        open with a one-way ticket to Paris. You can feel the panic of a woman
        who was ready to run.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_actions()

# KITCHEN
    def kitchen(self):
        os.system('cls')
        self.current_location = 'kitchen'

        print('''
    LOCATION: The Kitchen
        The scent of rosemary has been  replaced  by  the  stench  of  grease.
        Moonlight reflects off stainless steel knives—all clean, all  present.
        A liquor flask with Arthur's initials lies near a spilled sugar  bowl.
        On the counter sits a burnt  menu  for  a  "Celebratory Dinner"  dated
        the night of the murder.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_actions()

# LIBRARY
    def library(self):
        os.system('cls')
        self.current_location = 'library'

        print('''
    LOCATION: The Library
        Towering shelves lean inward like judges. A book on  'The  Biology  of
        Predators' lies open. On the desk, a secret  lover’s  photograph  lies
        face down, the lawyer’s smile curling in the dampness.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_actions()

    # NURSERY
    def nursery(self):
        os.system('cls')
        self.current_location = 'nursery'

        print('''
    LOCATION: The Nursery
        The bookshelf slides back. The air is freezing and smells of lavender.
        A detailed dollhouse sits in the center. Dead butterflies  are  pinned
        to the walls with surgical precision.

    PRESS ENTER TO CONTINUE\n''')

        self.display_actions()

# == ACTIONS ==
    def search(self):
        match self.current_location:

            case 'foyer': self.run_minigame(settings.foyer_searches, settings.foyer_dialogue, self.foyer_minigame_result, minigames.Minigames().anagram())
            case 'study': self.run_minigame(settings.study_searches, settings.study_dialogue, self.study_minigame_result, minigames.Minigames().numbrle())
            case 'bedroom': self.run_minigame(settings.bedroom_searches, settings.bedroom_dialogue, self.bedroom_minigame_result, minigames.Minigames().wordle())
            case 'library': self.run_minigame(settings.library_searches, settings.library_dialogue, self.library_minigame_result, minigames.Minigames().hangman())
            case 'kitchen': self.run_minigame(settings.kitchen_searches, settings.kitchen_dialogue, self.kitchen_minigame_result, minigames.Minigames().riddles())
            case 'nursery': self.run_minigame(settings.nursery_searches, settings.nursery_dialogue, self.nursery_minigame_result, minigames.Minigames().cryptic())

# == BTS ==
# TECHNICALITIES
    def display_actions(self):
        print('''    What would you like to do?
        ''')

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

        print('''    Where would you like to investigate next?
        ''')

        # Print locations
        for location in loc_wo_cur:
            print(f'        {loc_wo_cur.index(location)+1}. {location.capitalize()}')

        while True:
            room = input('\033[94m').lower()
            print('\033[0m', end='')

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
                print(colored(f'You are already in the {self.current_location.capitalize()}.', 'yellow'))
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

    def run_minigame(self, location_searches, dialogue, minigame_result, minigame):
        if location_searches > 0:
            print(dialogue)
            input('')
            minigame_result = minigame
        else:
            print(colored('Sorry, you have no more searches available for this room.','red'))