import random
from termcolor import colored

import dialogues
import settings
from settings import type_writer_print as print

class Minigames:
    def __init__(self):
        pass
    
    def hangman(self):
        print(dialogues.minigames['hangman']['instructions'])
        def making_a_guess():
            x = 0
            correct_guess = False
            for letter in chosen_word:
                if len(guess) > 1 or guess not in 'qwertyuiopasdfghjklzxcvbnm':
                    #makes sure that you can only enter one letter, and makes sure that what you entered is actually a letter
                    print (dialogues.minigames['hangman']['letter_error'])
                    correct_guess = True
                    break
                elif guess.lower() == chosen_word[x]:
                    if guess.lower()== blank_list [x]:
                        print(dialogues.minigames['hangman']['guessed_already_error'])
                        correct_guess=True
        #im making it true here because False adds a line to the hanged man meanwhile true does nothing, its just easier to do it this way :3
                        break
                    blank_list[x] = guess.lower()
                    correct_guess = True
                elif guess.lower() in wronglist:
                    print(dialogues.minigames['hangman']['guessed_already_error'])
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

        chosen_word = settings.hangman_answer

        blank = ""

        for letter in chosen_word:
            blank += "_"
        blank_list = list(blank)
        wronglist = []
        self.update_display = 0

        #----------------------------------------------------------------------------------------------

        print(HANGMANPICS[self.update_display])
        guess = input(f"Make a guess: ")
        making_a_guess()
        print(HANGMANPICS[self.update_display])
        print(''.join(blank_list))
        while self.update_display < 6:
            print(''.join(blank_list))
            if ''.join(blank_list) == chosen_word:
                return True 
            print('Wrong Letters: ')
            print(*wronglist, sep=', ')

            guess = input("Make a guess: ")
            making_a_guess()
            print(HANGMANPICS[self.update_display])
            print(''.join(blank_list))
        if self.update_display == 6:
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
            print(dialogues.minigames['wordle']['instructions'])
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
                    print(dialogues.minigames['wordle']['already_guessed_error'])
                    continue
                if not is_valid_guess(guess, guesses):
                    print(dialogues.minigames['wordle']['no_word_error'])
                    continue
                if guess == answers:
                    return True
                invalid.append(guess)
                feedback = evaluate_guess(guess, answers)
                attempts += 1
                
            
            if attempts > max_attempts:
                return False    
        guesses = []
        with open('guesses.txt', 'r') as file:
            guesses = [line.strip() for line in file]
        #this opens the dictionary that contains all the legal wordle words
        answers = settings.wordle_answer
        used_words  = []
        invalid = []
        
        return wordle(guesses, answers)

    def numbrle(self):
        print(dialogues.minigames['numbrle']['instructions'])
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
                gameActive = False
                return False
            else:

                try:
                    attempt = int(input('Please enter your number: '))
                except:
                    print(dialogues.minigames['numbrle']['error'])
                    continue

                if attempt > 9999 or attempt < 1000:
                    print(dialogues.minigames['numbrle']['error'])
                    continue

                attempt1 = str(int(attempt/1000))
                attempt2 = str(int(attempt / 100) - (int(attempt / 1000) * 10))
                attempt3 = str(int(attempt / 10) - (int(attempt / 100) * 10))
                attempt4 = str(int(attempt) - (int(attempt / 10) * 10))

                attempts = [int(attempt1), int(attempt2), int(attempt3), int(attempt4)]

                if len(set(attempts)) > 4 or len(set(attempts)) < 4:
                    print(dialogues.minigames['numbrle']['error'])
                    continue

                chanceCount += 1

                if attempt == number:
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
        Your guess: {attempt}
        There are {red} digit(s) in the correct position and {white} correct digit(s) in
        the wrong position.
        {chances - chanceCount} attempts remaining.\n''')

            count = 0
            red = 0
            white = 0

    def anagram(self):
        answer_list = list(settings.anagram_answer.upper())
        random.shuffle(answer_list)

        print(dialogues.minigames['anagram']['instructions'])

        answer= input("Write your answer: ").lower()

        for chances in range(4):
            if answer == settings.anagram_answer:
                return True
            elif answer != settings.anagram_answer:
                answer = input(dialogues.minigames['anagram']['error'])
        return False

    def cryptic(self):
        puzzles = {
        "PRMTWLN": "KINGDOM",
        "ULIVEVI": "FOREVER",
        "XLMGILO": "CONTROL"}

        code = random.choice(list(puzzles.keys()))
        answer = puzzles[code]

        print(dialogues.minigames['cryptic']['instructions'])
        print(f'''        Decode the word: {code}.
        ''')

        guess = input("Answer: ").strip().upper()

        for chances in range(4):
            if guess == answer:
                return True
            elif guess != answer:
                guess = input(dialogues.minigames['cryptic']['error'])
        return False

    def riddles(self):
        riddles_list = [
            ("I have a neck but no head, and I hold the spirit of Arthur. What am I?", settings.riddles_answer[0]),
            ("I am sharp and deadly, used to cut and slice, found in the kitchen where the maid works. What am I?", settings.riddles_answer[1]),
            ("I am small and sweet, spilled on the counter, near the flask of Arthur's favorite. What am I?", settings.riddles_answer[2])
        ]
        chosen_riddle, correct_answer = random.choice(riddles_list)
        print(dialogues.minigames['riddles']['instructions'])
        print(f'''        {chosen_riddle}
        ''')

        answer = input("Write your answer: ").lower()

        for chances in range(4):
            if answer == correct_answer:
                return True
            elif answer != correct_answer:
                answer = input(dialogues.minigames['riddles']['error'])
        return False