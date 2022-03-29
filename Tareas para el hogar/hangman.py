from platform import java_ver
import random
from telnetlib import NOP
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}


def arrojarPista(secretSet, secretWord):
    match secretSet:
        case 'Colors':
            if(secretWord in 'red yellow blue'):
                print('Es un color primario')
            elif(secretWord in 'black brown indigo'):
                print('Es un color oscuro')
            elif(secretWord in 'yellow orange green violet'):
                print('Es un color secundario')
            elif(secretWord == 'white'):
                print('Es un color muy claro')
        case 'Shapes':
            if(secretWord in 'square rectangle rhombus trapazoid'):
                print('Es una figura con cuatro lados')
            if(secretWord in 'circle ellipse'):
                print('Es una figura sin lados')
            if(secretWord in 'chevron pentagon hexagon septagon octogon'):
                print('Es una figura con mas de cuatro lados')
        case 'Fruits':
            if(secretWord in 'orange lemon lime grapefruit'):
                print('Es una fruta citrica')
            elif(secretWord in 'apple cherry strawberry tomato'):
                print('Es una fruta roja')
            elif(secretWord in 'pear banana'):
                print(
                    'Es una fruta amarillenta, pero no necesariamente del color amarillo')
            elif(secretWord in 'watermelon cantalope'):
                print('Es una fruta redonda y grande')
            elif(secretWord in 'grape'):
                print('Es una fruta violeta')
            elif(secretWord == 'mango'):
                print('Es una fruta anaranjada')

        case 'Animals':
            if(secretWord in 'bat bear deer dog donkey goat monkey panda rabbit rat sheep  whale wolf zebra weasel wombat moose otter skunk'):
                print('Es un animal mamifero')
            elif(secretWord in 'cat cougar lion tiger'):
                print('Es un animal felino')
            elif(secretWord in 'beaver mouse'):
                print('Es un animal roedor')
            elif(secretWord in 'duck eagle turkey owl'):
                print('Es un animal con plumas')
            elif(secretWord in 'crab fish shark squid leech'):
                print('Es un animal marino')
            elif(secretWord in 'python lizard turtle'):
                print('Es un animal reptil')
            elif(secretWord == 'frog'):
                print('Es un animal anfibio')


def getRandomWord(wordDict):
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.'''

    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# PROGRAMA PRINCIPAL
print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    arrojarPista(secretSet, secretWord)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
