import re

def numberGssr(x, y):
    print(f"Computer is going to try and guess your word from {x} to {y}")
    computerGuess = round((x + y)/2)
    previousLowerGuess = x
    previousHigherGuess = y

    while True:
        userFeedback = input(f"The computer guesses {computerGuess}, is that lower or higher than your actual number? If it is the correct number, write 'done': ")
        if userFeedback == 'lower' or userFeedback == 'l':
            previousHigherGuess = computerGuess
            computerGuess = round((computerGuess + previousLowerGuess) / 2)
        elif userFeedback == 'higher' or userFeedback == 'h':
            previousLowerGuess = computerGuess
            computerGuess = round((computerGuess + previousHigherGuess)/2)
        else:
            break

    print(f"The computer guessed your number {computerGuess}! Thank you for playing the game!")
            


userInput = input("Think of a random integer and then enter that integer's range, so that computer knows what numbers are possible: ")
userInput = re.findall('[0-9]+', userInput)

numberGssr(int(userInput[0]), int(userInput[1]))