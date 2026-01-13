import os

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.all_locations = ['library', 'suite', 'nursery']
        self.location_visited = []
        self.items = []

        self.introduction()
        
    def introduction(self):
        print('''
        Setting: Blackwood Manor, the night after Lord Alistair Blackwood is found dead in a locked study.
        The Conflict: Alistair was hours away from disinheriting his family to fund an orphanage.
        The Objective: Identify the killer before the police arrive.

        PRESS ENTER TO CONTINUE
        ''')
        input('')
        os.system('cls')
        self.foyer() # We will not include this line in this file, but in the character_story.py file

    def foyer(self):
        print('''
    LOCATION: The Grand Foyer
        In front of you lies The Will: A document on the table stating the estate goes to "The St. Jude Orphanage"
        tomorrow and The Argument Log: A servant’s diary noting a "violent shouting match" between Alistair and Arthur.

        Which room do you want to investigate first?
        ''')
        self.path() # We will not include this line in this file, but in the character_story.py file

    def path(self):
        counter = 1
        for location in self.all_locations:
            if location not in self.location_visited and len(self.location_visited) != 3:
                print(f'''{counter}. {location}''')
                counter += 1

        while True:
            room = input('').lower()
            if room in self.all_locations and room not in self.location_visited:
                self.location_visited.append(room)
                self.enter_room(room)
            elif room in self.location_visited:
                print(f'You have already visited {room}. Please choose another room.')
            else:
                print('Invalid room. Please try again.')

    def enter_room(self, room):
        pass
        # if room == '...':
            # room()