import random
import sys
import time
from termcolor import colored

import settings

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

class Minigames:
    def __init__(self):
        pass
    
    def hangman(self):
        def making_a_guess():
            x = 0
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
                self.update_display += 1
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

        chosen_word = str('ventilation')

        blank = ""

        for letter in chosen_word:
            blank += "_"
        blank_list = list(blank)
        wronglist = []
        self.update_display = 0

        #----------------------------------------------------------------------------------------------

        print(HANGMANPICS[self.update_display])
        guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
        making_a_guess()
        print(HANGMANPICS[self.update_display])
        print(''.join(blank_list))
        while self.update_display < 6:
            print(''.join(blank_list))
            if ''.join(blank_list) == chosen_word:
                print("You have obtained a clue!")
                return True 
            print('Wrong Letters: ')
            print(*wronglist, sep=', ')

            guess = input("Make another guess? ")
            making_a_guess()
            print(HANGMANPICS[self.update_display])
            print(''.join(blank_list))
        if self.update_display == 6:
            print("You failed to obtain the clue.")
            return False

    def wordle(self):
        def is_valid_guess(guess, guesses):
            return guess in guesses
        #this checks if your answer is a legal word or not
        def evaluate_guess(guess, word):
            str = ''
            for i in range(5):
                if guess[i] == word[i] :
                    str += '\033[32m' + guess[i]
                
                    #the \033[32m this makes your letter green if you guessed it correctly
                else: 
                    if guess[i] in word:
                        str += '\033[33m'+guess[i]
                        
                    #this makes your letter yellow if you got the letter right but not the location
                    else: 
                        str += '\033[0m'+guess[i]
                    
                    #keeps the colour defaut because it isnt in the letter
            used_words.append (str)
            return str + '\033[0m'
        def wordle(guesses, answers):
            print('Welcome to wordle! You have 6 attempts.')
            attempts = 1
            max_attempts = 6
            count = 1
            top = 5
            while attempts <= max_attempts:
                print('_________________\nUsed Words:')
                for i, a in enumerate(used_words):
                    print (a), 
                    if i % 5 == 4: 
                        print ('\n')
                #the i is the index starting from zero and a is the value of that index, i % 5 == 4 essentially means that every 5 items its going to make a \n (new row)
                #because the remainder of 4%5= 4, 9%5 = 4, 14%5 =4
                guess = input('\033[0mEnter Guess#'+str(attempts)+': ').lower()
                if guess in invalid:
                    print('Invalid Guess, you already guessed this word!')
                    continue
                if not is_valid_guess(guess, guesses):
                    print('Invalid Guess, please enter an english word with 5 letters!')
                    continue
                if guess == answers:
                    print('Congratulations, you got the clue!')
                    return True
                invalid.append(guess)
                feedback = evaluate_guess(guess, answers)
                attempts += 1
                
            
            if attempts > max_attempts:
                print ('GAME OVER, YOU FAILED')
                return False    
        guesses = []
        with open('guesses.txt', 'r') as file:
            guesses = [line.strip() for line in file]
        #this opens the dictionary that contains all the legal wordle words
        answers = ('plant')
        used_words  = []
        invalid = []
        
        return wordle(guesses, answers)

    def numbrle(self):
        chances = settings.numbrle_chances
        hasChance = True
        chanceCount = 0

        count = 0
        white = 0
        red = 0

        number = settings.numbrle_answer
        numbers = []

        for i in str(number):
            numbers.append(int(i))

        while hasChance:
            if chanceCount == chances:
                print("You have failed to guess the number.")
                print(f'The number was {number}')
                gameActive = False
                return False
            else:

                try:
                    attempt = int(input('Please enter your number: '))
                except:
                    print('Please enter a distinct four-digit number.')
                    continue

                if attempt > 9999 or attempt < 1000:
                    print('Please enter a distinct four-digit number.')
                    continue

                attempt1 = str(int(attempt/1000))
                attempt2 = str(int(attempt / 100) - (int(attempt / 1000) * 10))
                attempt3 = str(int(attempt / 10) - (int(attempt / 100) * 10))
                attempt4 = str(int(attempt) - (int(attempt / 10) * 10))

                attempts = [int(attempt1), int(attempt2), int(attempt3), int(attempt4)]

                if len(set(attempts)) > 4 or len(set(attempts)) < 4:
                    print('Please enter a distinct four-digit number.')
                    continue

                chanceCount += 1

                if attempt == number:
                    print('You have won the game. Congratulations.')
                    return True
                else:
                    for j in numbers:
                        for i in attempts:
                            if i == j:
                                # it exists
                                if j == attempts[count]:
                                    red += 1
                                else:
                                    white += 1
                            else:
                                # it doesn't exist
                                continue
                        count += 1
                    
                    print(f'''
        Your guess: {attempts}
        {red} Red
        {white} White
        {chances - chanceCount} attempts remaining.\n''')

            count = 0
            red = 0
            white = 0

    def anagram(self):
        print('''        Turn these letters to make new existing word: A-S-T-U-T-E-R.
        You only have 5 chances to guess the word, if you  fail  you  won't  be
        able to obtain the clue.Think wisely before answering, the fate  is  in
        your hand
        ''')

        answer= input("Write your answer: ").lower()

        for chances in range(4):
            if answer == "stature":
                print('CORRECT')
                return True
            elif answer != "stature":
                answer = input(colored('The answer is still incorrect, try again:\n','red'))
        return False

    def cryptic(self):
        print('running game cryptic')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False

    def riddles(self):
        print('running game riddles')
        succeed = input('y/n')
        if succeed == 'y':
            return True
        elif succeed == 'n':
            return False
