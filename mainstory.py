import os

# This will be the main storyline, choices that do not depend on the character chosen
class Story:
    def __init__(self):
        self.introduction()
        
    def introduction(self):
        print('''
        Setting: Blackwood Manor, the night after Lord Alistair Blackwood is found dead in a locked study.
        The Conflict: Alistair was hours away from disinheriting his family to fund an orphanage.
        The Objective: Identify the killer before the police arrive.

        CLICK ENTER TO CONTINUE
        ''')
        input('')
        os.system('cls')
        self.foyer()

    def foyer(self):
        print('''
    LOCATION: The Grand Foyer
        In front of you lies The Will: A document on the table stating the estate goes to "The St. Jude Orphanage"
        tomorrow and The Argument Log: A servant’s diary noting a "violent shouting match" between Alistair and Arthur.

        Which room do you want to investigate first?
        ''')
        self.path()

    def path(self):
        all_locations = ['library', 'suite', 'nursery']
        location_visited = ['library', 'suite']
        counter = 1
        for location in all_locations:
            if location not in location_visited and len(location_visited) != 3:
                print(f'''{counter}. {location}''')
                counter += 1

        while True:
            room = input('').lower()