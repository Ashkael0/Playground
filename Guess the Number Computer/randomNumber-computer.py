import random

randomNumber = random.randrange(0,100)

while True:
	guess = int(input('Try to guess the number: '))
	if guess < randomNumber:
		print('Guess higher!')
	elif guess > randomNumber:
		print('Guess lower!')
	else:
		print('Congratulations, you got it!')
		break