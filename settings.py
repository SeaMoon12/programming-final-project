# Print speed
print_speed = 0

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
        'minigame': 'riddle',
        'searches': 3,
        'isKeyRoom': False
    },
    'nursery': {
        'minigame': 'cryptic',
        'searches': 3,
        'isKeyRoom': False
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
