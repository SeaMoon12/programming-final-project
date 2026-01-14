import random
class Minigames:
    def __init__(self):
        pass
    def hangman(self):
        print('running game hangman')
        HANGMANPICS= ['''
             +---+
             |   |
                 |
                 |
                 |
                 |
            ======''','''
             +---+
             |   |
             O   |
                 |
                 |
                 |
            ======''','''
             +---+
             |   |
             O   |
             |   |
                 |
                 |
            ======''','''
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
            ======''', '''
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
            ======''','''
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
            ======''',
            '''
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
            ======'''
        ]
        WORDS='VENTILATION'.split()

        def getRandomWord(wordList):
            wordIndex=random.randint(0,len(wordList)-1)
            return wordList[wordIndex]
        #This gets a random word from the WORDS list, but currently it only has one word
        def displayBoard(missedLetters, correctLetters, secretWord):
            print(HANGMANPICS[len(missedLetters)])
            print()
            #this prints the ascii images of the hanged man
            print('Missed Letters: ', end='')
            for letter in missedLetters:
                print(letter, end='')
            print()
            def getGuess(alreadyGuessed):
                #returns the letter that the player inputted, this makes sure that its a single letter
                while True:
                    print('Guess a letter')
                    guess=input()
                    guess=guess.lower()
                    if len(guess) !=1:
                        print('Please enter a single letter.')
                    elif guess in alreadyGuessed:
                        print('You already guess that letter, choose again')
                    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                        print('please enter a LETTER!')
                    else:
                        return guess
            print('H A N G M A N')
            missedLetters=''
            correctLetters=''
            secretWord=getRandomWord(WORDS)
            while True:
                displayBoard(missedLetters,correctLetters,secretWord)
                #allows the player to enter a letter
                guess=getGuess(missedLetters+correctLetters)
                if guess in secretWord:
                    correctLetters=correctLetters=+guess
                    #checks if the player has won
                    foundAllLetters=True
                    for i in range(len(secretWord)):
                        if secretWord[i] not in correctLetters:
                            foundAllLetters=False
                            break
                    if foundAllLetters:
                        print('Congratulations! You have got a clue:'+secretWord)
                    else:
                        missedLetters=missedLetters=+guess
                        if len(missedLetters)==len(HANGMANPICS)-1:
                            print('YOU FAILED TO UNCOVER THE CLUE...')
    def wordle(self):
        print('running game wordle')
    def numbrle(self):
        print('running game numbrle')
    def scramble(self):
        print('running game scramble')
    def anagram(self):
        print('running game anagram')
    def cryptic(self):
        print('running game cryptic')
    def riddles(self):
        print('running game riddles')
