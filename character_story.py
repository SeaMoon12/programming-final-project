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
    def __init__(self):
        self.role = 'paranormal'
        super().__init__()

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
            self.found_brochure = True
            print('''
        You examine the vent slats. They are bent outward. You crack the  safe
        You sit in the chair. Suddenly, you can't move. Your limbs  are  lead.
        You hear a click from the wall behind you. "I'm  fixing you, Grandpa."
        You find a Boarding School Brochure inside the  safe-Alistair’s  death
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
            self.found_glove = True

            print('''
        As you touch the fabric, the air turns ice-cold. You don't just see  a
        glove; you feel the small, frantic breathing of a child hiding in  the
        dark. A whisper crawls into your ear: 'The walls have eyes... and I am
        the eyes.' The glove feels like a physical piece of  a  haunting  that
        hasn't yet left the manor.

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
        self.special_use = settings.investigator_searches
        self.role = 'investigator'
        super().__init__()

    # FOYER
    def foyer(self):
        super().foyer()

        if self.foyer_minigame_result == True:
            print('''
        You click your pen, measuring the arc of the brownish  spray.  Physics
        don't lie: the height is exactly 36 inches. You note  that  Arthur  is
        nearly six feet tall. While he was seen  arguing  here,  the  physical
        trajectory of this blood doesn't align with his height or  a  standing
        struggle.
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
            self.found_brochure = True
            print('''
        The safe door swings open. Among  the  legal  documents,  you  find  a
        glossy brochure for a strict international reform school. You note the
        date on the postmark: it was delivered the very morning of the murder.
        Unlike the other suspects' motives, which were  simmering  for  years,
        this was an immediate trigger. You see the bent vent slats behind  the
        desk and realize the chair Alistair died in was  perfectly  positioned
        for an attack from the wall.
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
        You pull up the loose floorboard. Beneath it lies  the  bloody  letter
        opener and Arthur’s bloody IOU. It’s the perfect crime scene,  exactly
        as described in the  8-year-old  cold  case  file.  'A frame-up,'  you
        mutter, noting how conveniently  these  items  are  grouped  together.

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
        You pry the hatch open  with  a  crowbar.  Inside  the  gears  of  the
        dumbwaiter, you find a Bribe Ledger. It contains records  of  payments
        made by the family lawyer to local  precincts  to  'overlook'  certain
        details in the 2018 report. The names are redacted, but the intent  to
        bury the truth is clear.
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
            self.found_glove = True
            print('''
        The You shine your light into the duct. The dust has  been  disturbed
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

    def display_rooms(self):
        while True:
            if self.special_use > 0 and self.searching:
                self.searching = False
                choice = input(f'''Use Authority Check? (Remaining: {self.special_use})''').lower()
                if choice == 'y' or choice == 'yes':
                    self.special_use -= 1
                    match self.current_location:
                        # FOYER
                        case 'foyer':
                            print('''
        You apply a luminol reagent to the baseboards. The spray pattern isn't
        just low; it’s static and concentrated. This wasn't  a  wound  from  a
        fight; it was an arterial spray from a victim who was already down  or
        a killer who was striking from a fixed, low position. You spot a faint
        indentation in the floor dust where a heavy,  small  object-perhaps  a
        step-stool-was recently placed and removed
                            \n    PRESS ENTER TO CONTINUE''')
                            input('')
                            break

                        # STUDY
                        case 'study':
                            print('''
        You examine the brochure under your magnifying  glass.  You  notice  a
        wax-like residue on the  pages-remnants  of  a  child's  crayon.  More
        importantly,  you  see  the  enrollment  form  is  already  signed  by
        Alistair. Your professional instinct connects  the  dots:  the  killer
        didn't just find this; they were in the room when Alistair signed  his
        own death warrant.
                            \n    PRESS ENTER TO CONTINUE''')
                            input('')
                            break

                        # BEDROOM
                        case 'bedroom':
                            print('''
        You examine the letter opener with a magnifying lens. The blood on the
        blade is clotted incorrectly for an 8-year-old stain; it looks like it
        was applied much later to 'refresh' the evidence. You notice a Size  4
        footprint in the undisturbed dust deep under the  joists.  The  killer
        didn't just hide the weapon here; they've been returning to this spot,
        perhaps to ensure the 'truth' remained exactly where  they  wanted  it
        found.
                            \n    PRESS ENTER TO CONTINUE''')

                        # KITCHEN
                        case 'kitchen':
                            print('''
        You flip to the back of the ledger and find a loose evidence  log.  It
        details 'child-sized footprints' found in the kitchen grease that were
        never photographed for the  official  file.  You  cross-reference  the
        ledger's dates with the family travel records; while the  adults  were
        accounted for, the 'little one' was always left behind in  the  manor.
        The  corruption  wasn' t  protecting  the  son  or  the  wife-it   was
        protecting the estate's image from the actions of a child.
                            ''')

                        # LIBRARY
                        case 'library':
                            print('''
        You rub the  fabric  between  your  fingers.  It’s  cheap,  reinforced
        cotton-the exact grade used in  local  school  uniforms.  You  find  a
        faint, ink-stamped 'L' on the inner wrist. This isn't  just  a  'small
        person'; this is evidence  of  a  child  meticulously  navigating  the
        manor's guts.
                            \n    PRESS ENTER TO CONTINUE''')
                            input('')
                            break
                elif choice == 'n' or choice == 'no':
                    break
                else:
                    print('Please answer with \'yes\' or \'no\'.')
            else:
                break
                    
        super().display_rooms()

class StoryBuyer(mainstory.Story):
    def __init__(self):
        self.role = 'buyer'
        super().__init__()

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
            self.found_brochure = True
            print('''
        You use the safe code found in your  hidden  blueprints.  Inside,  the
        brochure explains why the room was so carefully  mapped.  Lily  wasn't
        killing for money; she was protecting her territory. You  realize  the
        'monster' the lawyers were paid to hide is still here, and she  killed
        to ensure she would never have to leave.
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
            self.found_glove = True

            print('''
        You consult your blueprints and realize this vent isn't just for  air;
        it’s a structural blind spot that connects the Library directly to the
        Study chair. Finding this tiny glove confirms your  fear:  someone  of
        small stature has been moving through the very  veins  of  your  house
        like a parasite.

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
