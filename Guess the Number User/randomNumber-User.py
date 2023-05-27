import re

# Numbers x and y will be inputted by the user in the userInput's function 
def numberGssr(x, y):
    print(f"Computer is going to try and guess your word from {x} to {y}")
    
    # The round() function uses 'banker's rounding', where 'x.5' number gets rounded to the nearest EVEN number
    # So sometimes it will round up and sometimes it will round down, depending where the even number is
    # This property will make our function work even when the 'hidden' number is the smallest or the largest
    # possible number in our provided range
    computerGuess = round((x + y)/2)

	
    # lowerBound tracks the lower bound of the range where the 'secret' number can be
    lowerBound = x

	# higherBound tracks the higher bound of the range where the 'secret' number can be
    higherBound = y

    while True:
        userFeedback = input(f"The computer guesses {computerGuess}, is that lower or higher than your actual number? If it is the correct number, write 'done': ")
        if userFeedback == 'lower' or userFeedback == 'l':

			# If the user said that their number is lower than the current guess,
			# that means that the curent computer guess is the upper bound
			# of where the number can possibly be.
            higherBound = computerGuess
            computerGuess = round((computerGuess + lowerBound) / 2)
        elif userFeedback == 'higher' or userFeedback == 'h':
            
            # If the user said that their number is higher than the current guess,
			# that means that the curent computer guess is the lower bound
			# of where the number can possibly be.
            lowerBound = computerGuess
            computerGuess = round((computerGuess + higherBound)/2)
        else:
            break

    print(f"The computer guessed your number {computerGuess}! Thank you for playing the game!")
            


userInput = input("Think of a random integer and then enter that integer's range, so that computer knows what numbers are possible: ")
userInput = re.findall('[0-9]+', userInput)

numberGssr(int(userInput[0]), int(userInput[1]))