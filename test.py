#hangman
import random
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if len(guess) > 1 or guess not in 'qwertyuiopasdfghjklzxcvbnm':
            #makes sure that you can only enter one letter, and makes sure that what you entered is actually a letter
            print ('please enter one(1) letter')
            correct_guess = True
            break
        elif guess.lower() == chosen_word[x]:
            if guess.lower()== blank_list [x]:
                print('You already guessed this letter!')
                correct_guess=True
#im making it true here because False adds a line to the hanged man meanwhile true does nothing, its just easier to do it this way :3
                break
            blank_list[x] = guess.lower()
            correct_guess = True
        elif guess.lower() in wronglist:
            print('you already guessed this letter!')
            correct_guess=True 
            break
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        wronglist.append(f'{guess.lower()}')
        update_display += 1
    x = 0


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["ventilation"]

chosen_word = list(random.choice(word_list))

blank = ""

for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
wronglist = []
update_display = 0

#----------------------------------------------------------------------------------------------

print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("You have obtained a clue!")
        break
    print('Wrong Letters: ')
    print(*wronglist, sep=', ')

    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print("You failed to obtain the clue.")