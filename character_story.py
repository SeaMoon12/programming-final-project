# If there are events that may happen, this class will allow these events to happen based on the character chosen
from termcolor import colored
import os
import mainstory
import minigames

class StoryParanormal(mainstory.Story):
    # FOYER
    def foyer(self):
        super().foyer()

        print('''
        As you gaze on the wall, you find yourself trembling at the sight of
        
            a low BLOOD splatter
        
        You hear a faint whistle mumbling the words
            On... his... knees...
        
    PRESS ENTER TO CONTINUE''')
        input('')

        self.path()

    # STUDY
    def study(self):
        super().study()

        print('''        Despite trying so hard to find the combination, you could not find the right combination.
        You hear a whisper like a wind

            tea... tasted... sleep...

    PRESS ENTER TO CONTINUE''')
        input('')

        self.path()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        print('''
        As you take a closer look, you hear a faint voice...
        
            Staged... all... staged...

    PRESS ENTER TO CONTINUE
    ''')
        input('')

        self.path()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.path()

    # LIBRARY
    def library(self):
        os.system('cls')
        self.current_location = 'library'

        print('''
    LOCATION: The Library
        Stepping into the library, you browse through all the books available when you stumble upon a photo.
        It turns out that Elara had a secret lover: The Lawyer. Her husband had not known anything about this.
        After going through several book isles, you found a marriage contract between Alistair and his wife.
        It says that if Elara ever had a divorce with him, Elara would lose everything.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.path()

    # NURSERY
    def nursery(self):
        super().nursery()
        self.path()

class StoryDetective(mainstory.Story):
    # FOYER
    def foyer(self):
        super().foyer()

        print('''
        As you gaze on the wall, you find a low blood splatter.
        You use your detective tools and find a size 9 boot print in the dust.
        Coincidentally, size 9 is the same size as Arthur's foot.

    PRESS ENTER TO CONTINUE''')
        input('')

        self.path()
    # STUDY
    def study(self):
        super().study()

        minigames.Minigames().numbrle()

        print('''
        After cracking the combination to the safe, you find a book that reads 'A Poisoner's Guide'.
        You thought, "maybe Elara used this to poison Alistair."

    PRESS ENTER TO CONTINUE''')
        input('')

        self.path()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        print('''        "Aha! This letter opener is the murder weapon!"
        ''')

        self.path()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.path()

    # LIBRARY
    def library(self):
        super().library()

        print('''
        After close inspection upon the walls of the library, you find a strand
        of long, blonde hair, caught in the grate of the ventilation. It belongs
        to Elara, Alistair's wife. It looks like she was spying on something...
        or someone...
        
    PRESS ENTER TO CONTINUE''')

        input('')

        self.path()

    # NURSERY
    def nursery(self):
        super().nursery()
        self.path()

class StoryBuyer(mainstory.Story):
    def foyer(self):
        super().foyer()
    # FOYER
        print('''
        As you gaze on the wall, you find yourself trembling at the sight of

            a low BLOOD splatter

        As you pull out your blueprint, you notice something missing from the room: A hidden step-stool nook.

            "Why would anyone need a stool here?", you thought

    PRESS ENTER TO CONTINUE''')

        input('')

        self.path()

    # STUDY
    def study(self):
        super().study()

        print('''        You pulled out the blueprint and after close inspection and comparison, the blueprint seems
        to show a hidden crawlspace directly above the desk chair.

    PRESS ENTER TO CONTINUE''')
        input('')
        self.path()

    # BEDROOM
    def bedroom(self):
        super().bedroom()
        self.path()

    # KITCHEN
    def kitchen(self):
        super().kitchen()
        self.path()

    # LIBRARY
    def library(self):
        super().library()
        
        if 'nursery' not in self.all_locations:
            self.all_locations = ['foyer', 'study', 'bedroom', 'kitchen', 'library', 'nursery']
            print('''
        After close inspection upon the blueprint of the mansion, you find a
        hidden room next to the library. After following the direction of the
        room, you find a ventilation space, leading away from the library. It
        appears to be a nursery.''')

            print(colored('''
        You now have access to The Nursery.
            ''', 'green'))

        print('    PRESS ENTER TO CONTINUE')
        input('')

        self.path()

    # NURSERY
    def nursery(self):
        super().nursery()
        self.path()