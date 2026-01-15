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

        if self.foyer_minigame_result == True:
            print('''
        The air turns ice-cold. A whisper crawls into your ear: "He... knelt...
        begging for gold... but the shadow stood above us  both."  You  realize
        the blood splatter stops at  three  feet.  Arthur  was  kneeling  here,
        begging, but he wasn't the one who bled.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.foyer_minigame_result == False:
            print('''
        The shadows dance, mocking your eyes. The stain  is  just  a  stain, a
        senseless blotch on a ruined house.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        
        self.foyer_minigame_result = None
        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            print('''
        You examine the vent slats. They are bent outward. You crack the  safe
        You sit in the chair. Suddenly, you can't move. Your limbs  are  lead.
        You hear a click from the wall behind you. "I'm  fixing you, Grandpa."
        You find a Boarding School Brochure inside the  safe—Alistair’s  death
        warrant.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.study_minigame_result == False:
            print('''
        The safe jams. You stare at the  vent  behind  the  chair, and  for  a
        second, you see a pair of unblinking eyes watching you.  You  are  not
        alone in this room.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.study_minigame_result = None
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print('''
        You hear Elara’s sobbing. "I didn't do it! I only wanted him to sleep!"
        You reach under the board and find  a  bloody  letter  opener. But  the
        blood feels... wrong. It’s a stage prop, meant to be found.

        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.bedroom_minigame_result == False:
            print('''
        A shower of plaster dust falls from the ceiling. You  pull  your  hand
        back. The darkness under the floor seems to grow teeth. You leave  the
        secret buried.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.bedroom_minigame_result = None
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print('''
        You touch the iron door and hear the clinking of glass from the  past.
        "A  spoonful  for  sleep...  a  spoonful  for  my  escape."  You  feel 
        Elara's frantic heartbeat. Inside the hatch, you  find  empty  blister
        packs of sleeping pills. She drugged him.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.kitchen_minigame_result == False:
            print('''
        The pulley snaps with a violent bang. The  hatch  is  jammed  forever,
        burying the truth in the basement's dark.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.kitchen_minigame_result = None
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        if self.library_minigame_result == True:
            print('''
        You hear the sound of small, frantic breathing inside  the  wall. "The
        walls have eyes... and I am the eyes." You reach in  and  pull  out  a
        strand of white silk. It feels like spiderweb, but it's from a child's
        dress.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.library_minigame_result == False:
            print('''
        A low hiss echoes from the duct. You recoil, and the iron grate  seems
        to fuse shut. The house refuses to show you its veins.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.library_minigame_result = None
        self.display_rooms()

class StoryPrivateInvestigator(mainstory.Story):
    def __init__(self):
        super().__init__()
        self.special_use = settings.investigator_searches

    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print('''
        You click your pen, measuring the arc of  the  spray.  "Physics  don't
        lie," you mutter. The height is exactly 36 inches. Arthur  is  a  head
        taller than his father. Whoever caused this splatter was  either  very
        short or positioned in the shadows.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.foyer_minigame_result == False:
            print('''
        The shadows dance, mocking your eyes. The stain  is  just  a  stain, a
        senseless blotch on a ruined house.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.foyer_minigame_result = None
        self.display_rooms()
    
    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            print('''
        You examine the vent slats. They are bent outward. You crack the  safe
        and find architectural sketches of the vent system, drawn  in  crayon.
        The murder was committed from inside the wall  while  the  victim  was
        sedated.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.study_minigame_result == False:
            print('''
        The safe jams. You stare at the vent  behind  the  chair,  and  for  a
        second, you see a pair of unblinking eyes watching  you. You  are  not
        alone in this room.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.study_minigame_result = None
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print('''
        You pull up the board. You find the letter opener and Arthur’s  bloody
        IOU. It’s too perfect. "A frame-up," you mutter. You  find  a  Size  4
        footprint in the dust beneath the floorboards.

        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.bedroom_minigame_result == False:
            print('''
        A shower of plaster dust falls from the ceiling. You  pull  your  hand
        back. The darkness under the floor seems to grow teeth. You leave  the
        secret buried.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.bedroom_minigame_result = None
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print('''
        You pry the hatch open with a crowbar. Inside, among the gears,  is  a
        Bribe Ledger. It shows the family lawyer paid  the  police  to  ignore
        "child-sized footprints" found in this kitchen. The corruption runs as
        deep as the grease.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.kitchen_minigame_result == False:
            print('''
        The pulley snaps with a violent bang. The  hatch  is  jammed  forever,
        burying the truth in the basement's dark.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.kitchen_minigame_result = None
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        if self.library_minigame_result == True:
            print('''
        You hear the  sound  of  small, frantic  breathing  inside  the  wall.
        "The You shine your light into the duct. The dust has  been  disturbed
        by small hands and knees. You find a Size 4 glove snagged on  a  bolt.
        This isn't a vent; it's a highway for a ghost that breathes.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.library_minigame_result == False:
            print('''
        A low hiss echoes from the duct. You recoil, and the iron grate  seems
        to fuse shut. The house refuses to show you its veins.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.library_minigame_result = None
        self.display_rooms()

class StoryBuyer(mainstory.Story):
    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print('''
        You consult the tattered blueprint. There’s a hollow space in the wall
        - a step-stool nook. You realize someone small stoodhere to watch the
        argument, or perhaps to participate in it.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.foyer_minigame_result == False:
            print('''
        The shadows dance, mocking your eyes. The stain  is  just  a  stain, a
        senseless blotch on a ruined house.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.foyer_minigame_result = None
        self.display_rooms()

    # STUDY
    def study(self):
        super().study()

        if self.study_minigame_result == True:
            print('''
        You open the safe using the  code  from  the  blueprint. Inside  is  a
        Disinheritance Deed. Arthur was going to be homeless; Lily  was  going
        to be locked away. Both had a reason to want him  dead, but  only  one
        had the map.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.study_minigame_result == False:
            print('''
        The safe jams. You stare at the  vent  behind  the  chair, and  for  a
        second, you see a pair of unblinking eyes watching  you. You  are  not
        alone in this room.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.study_minigame_result = None
        self.display_rooms()

    # BEDROOM
    def bedroom(self):
        super().bedroom()

        if self.bedroom_minigame_result == True:
            print('''
        You  find  the  letter  opener.  According  to  your  blueprint,  this
        floorboard is directly above a vent  junction.  Someone  dropped  this
        here from the Library to ensure Elara would take the fall.

        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.bedroom_minigame_result == False:
            print('''
        A shower of plaster dust falls from the ceiling. You  pull  your  hand
        back. The darkness under the floor seems to grow teeth. You leave  the
        secret buried.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.bedroom_minigame_result = None
        self.display_rooms()

    # KITCHEN
    def kitchen(self):
        super().kitchen()

        if self.kitchen_minigame_result == True:
            print('''
        Your blueprint shows the dumbwaiter shaft runs parallel to the Library
        vents. You find a discarded tea tin inside, hidden away. It  reeks  of
        sedatives. You realize the "happy meal" Elara  prepared  was  a  trap.
        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.kitchen_minigame_result == False:
            print('''
        The pulley snaps with a violent bang. The  hatch  is  jammed  forever,
        burying the truth in the basement's dark.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.kitchen_minigame_result = None
        self.display_rooms()

    # LIBRARY
    def library(self):
        super().library()

        if self.library_minigame_result == True:
            print('''
        You hear the sound of small, frantic breathing inside  the  wall. "The
        The blueprint reveals  the  truth:  this  vent  connects  the  Library
        directly to the Study chair. You find a small  latch  on  the  inside.
        Someone was moving through your house like a parasite.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

            self.all_locations.append('nursery')

            print(colored('You now have access to the Nursery\n', 'green'))

        elif self.library_minigame_result == False:
            print('''
        A low hiss echoes from the duct. You recoil, and the iron grate  seems
        to fuse shut. The house refuses to show you its veins.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.library_minigame_result = None
        self.display_rooms()

    # NURSERY
    def nursery(self):
        super().nursery()

        if self.nursery_minigame_result == True:
            print('''
        The diary opens. 'Elara gave him the  sleep-tea.  Arthur  screamed  at
        him. They are so loud. I used the silver  needle  tonight.  He  didn't
        make a sound. Now I can stay in my house  forever.' You  realize  Lily
        has been living in the walls for 8 years, watching you.

        \n    PRESS ENTER TO CONTINUE''')
            input('')
        elif self.nursery_minigame_result == False:
            print('''
        The letters squirm like  insects. Your  nose  bleeds  from  the  sheer
        malice in the room. You slam the book shut, but the feeling  of  being
        watched remains.
        \n    PRESS ENTER TO CONTINUE''')
            input('')

        self.nursery_minigame_result = None
        self.display_rooms()