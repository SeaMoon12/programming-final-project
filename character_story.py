from termcolor import colored
import os
import sys
import time

import settings
import mainstory
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
    # FOYER
    def foyer(self):
        super().foyer()

        if self.mini_result == True:
            print('''
        The air turns ice-cold. A whisper crawls into your ear: "He... knelt...
        begging for gold... but the shadow stood above us  both."  You  realize
        the blood splatter stops at  three  feet.  Arthur  was  kneeling  here,
        begging, but he wasn't the one who bled.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        else:
            print('''
        The shadows dance, mocking your eyes. The  stain  is  just  a  stain, a
        senseless blotch on a ruined house.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        print('''        Despite trying so hard to find the combination, you could not find the right combination.
        You hear a whisper like a wind

            tea... tasted... sleep...
        \n    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        print('''
        As you take a closer look, you hear a faint voice...
        
            Staged... all... staged...
        \n    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().kitchen()
        self.display_rooms()

class StoryPrivateInvestigator(mainstory.Story):
    # FOYER
    def foyer(self):
        super().foyer()

        print('''
        As you gaze on the wall, you find a low blood splatter.
        You use your tools and find a size 9 boot print in the dust.
        Coincidentally, size 9 is the same size as Arthur's foot.
        \n    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_rooms()
    
    # STUDY
    def study(self):
        super().study()

        minigames.Minigames().numbrle()

        print('''
        After cracking the combination to the safe, you find a book that reads 'A Poisoner's Guide'.
        You thought, "maybe Elara used this to poison Alistair."
        \n    PRESS ENTER TO CONTINUE''')
        input('')

        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        print('''
        After close inspection upon the walls of the library, you find a strand
        of long, blonde hair, caught in the grate of the ventilation. It belongs
        to Elara, Alistair's wife. It looks like she was spying on something...
        or someone...
        \n    PRESS ENTER TO CONTINUE''')

        input('')

        self.display_rooms()

class StoryBuyer(mainstory.Story):
    # FOYER
    def foyer(self):
        super().foyer()
        print('''
        As you gaze on the wall, you find yourself trembling at the sight of

            a low BLOOD splatter

        As you pull out your blueprint, you notice something missing from the room: A hidden step-stool nook.

            "Why would anyone need a stool here?", you thought
        \n    PRESS ENTER TO CONTINUE''')

        input('')

        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        print('''        Despite trying so hard to find the combination, you could not find the right combination.
        You pulled out the blueprint and after close inspection and comparison, the blueprint seems
        to show a hidden crawlspace directly above the desk chair.
        \n    PRESS ENTER TO CONTINUE''')
        input('')
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()
        self.display_rooms()

    # NURSERY
    def nursery(self):
        super().nursery()
        self.display_rooms()