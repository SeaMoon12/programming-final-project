# If there are events that may happen, this class will allow these events to happen based on the character chosen
import mainstory

class StoryParanormal(mainstory.Story):
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
    def study(self):
        super().study()
        self.path()
    def bedroom(self):
        super().bedroom()
        self.path()
    def kitchen(self):
        super().kitchen()
        self.path()
    def library(self):
        super().library()
        self.path()
    def nursery(self):
        super().nursery()
        self.path()

class StoryDetective(mainstory.Story):
    def foyer(self):
        super().foyer()

        print('''
        As you gaze on the wall, you find a low blood splatter.
        You use your detective tools and find a size 9 boot print in the dust.
        Coincidentally, size 9 is the same size as Arthur's foot.

    PRESS ENTER TO CONTINUE''')

        input('')

        self.path()
    def study(self):
        super().study()
        self.path()
    def bedroom(self):
        super().bedroom()
        self.path()
    def kitchen(self):
        super().kitchen()
        self.path()
    def library(self):
        super().library()
        self.path()
    def nursery(self):
        super().nursery()
        self.path()

class StoryBuyer(mainstory.Story):
    def foyer(self):
        super().foyer()

        print('''
        As you gaze on the wall, you find yourself trembling at the sight of

            a low BLOOD splatter

        As you pull out your blueprint, you notice something missing from the room: A hidden step-stool nook.

            "Why would anyone need a stool here?", you thought

    PRESS ENTER TO CONTINUE''')

        input('')

        self.path()
    def study(self):
        super().study()
        self.path()
    def bedroom(self):
        super().bedroom()
        self.path()
    def kitchen(self):
        super().kitchen()
        self.path()
    def library(self):
        super().library()
        self.path()
    def nursery(self):
        super().nursery()
        self.path()