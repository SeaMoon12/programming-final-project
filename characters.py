class Characters:
    def __init__(self):
        self.items = []
        self.role = None # used so we can execute events *IF* the player chose the certain role


class Paranormal(Characters):
    def __init__(self):
        super().__init__()
        self.role = 'paranormal'

class Detective(Characters):
    def __init__(self):
        super().__init__()
        self.role = 'detective'

class Buyer(Characters):
    def __init__(self):
        super().__init__()
        self.items.append('blueprint')
        self.role = 'buyer'