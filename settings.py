import sys
import time

# Print speed
print_speed = 0

def type_writer_print(*args, **kwargs):
    # Extract speed settings if provided, otherwise use defaults
    speed = kwargs.pop('speed', print_speed)
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

room_config = {
    'foyer': {
        'minigame': 'anagram',
        'searches': 3,
        'isKeyRoom': False,
    },
    'study': {
        'minigame': 'numbrle',
        'searches': 3,
        'isKeyRoom': True,
        'keyClue': 'found_brochure'
    },
    'bedroom': {
        'minigame': 'wordle',
        'searches': 3,
        'isKeyRoom': False
    },
    'library': {
        'minigame': 'hangman',
        'searches': 3,
        'isKeyRoom': True,
        'keyClue': 'found_glove',
        'unlocks': 'nursery'
    },
    'kitchen': {
        'minigame': 'riddles',
        'searches': 3,
        'isKeyRoom': False
    },
    'nursery': {
        'minigame': 'cryptic',
        'searches': 3,
        'isKeyRoom': False,
        'isHidden': True
    }
}

# Limit
searches = 3
investigator_searches = 1

# Settings for minigames
numbrle_chances = 10

# Answers to the minigames
hangman_answer = 'ventilation'
wordle_answer = 'plant'
numbrle_answer = 4261
anagram_answer = 'stature'
cryptic_answer = None
riddle_answer = ['liquor flask', 'knife', 'sugar']
