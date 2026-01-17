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

# Limit
searches = 3
foyer_searches = 3
study_searches = 3
bedroom_searches = 3
kitchen_searches = 3
library_searches = 3
nursery_searches = 3
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
