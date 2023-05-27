import random
from words import words
import math

def playHangman():
    randomWord = random.choice(words).upper()
    unguessedLetters = set(randomWord)
    censoredWord=['__' for letter in randomWord]
    wordLength = len(randomWord)
    lives = 4 + round(len(randomWord)/math.pi)
    print(f"Your word consists of {wordLength} letters and you were given {lives} lives to solve it.")
    guessedLetters = set()
    while '__' in censoredWord and lives > 0:
        print(f"{' '.join(censoredWord)}")
        while True:
            if len(guessedLetters) > 0:
                 print(f"You already guessed these letters: {' '.join(guessedLetters)}")
            print(f"You have {lives} lives remaining.")
            userGuess = input("Input your guess: ").upper()
            if userGuess.isalpha():
                 break
            print(f"Your guess {userGuess} is not valid alphabetical number, try again.")
        if userGuess in guessedLetters:
             print(f"You already guessed {userGuess}, guess another letter.")
             continue
        else:
             guessedLetters.add(userGuess)
        randomWordList = list(randomWord)
        if userGuess not in randomWordList:
             lives -= 1
             print(f"Sorry letter {userGuess} is not part of the word, you have {lives} lives remaining.")             
        censoredWord = [letter if letter in guessedLetters else "__" for letter in randomWord]
    if lives > 0:
         print(f"Congratulations, you guessed the word {' '.join(censoredWord)}")
    else:
         print(f"You ran out of lives, the correct word was {randomWord}")

playHangman()

