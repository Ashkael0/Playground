import random

def rockPaperScissors():
    userChoice = input(f"Input (R) if you want to play Rock, (P) if you want to play Paper, and (S) if you wan to play Scissors: ").lower()
    computerChoice = random.choice(['r', 'p', 's'])
    print(f"The computer's guess is {computerChoice}")
    if (userChoice == 'r' and computerChoice == 's') or (userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p'):
        return print("Congratulations, you won!")
    elif (computerChoice == 'r' and userChoice == 's') or (computerChoice == 'p' and userChoice == 'r') or (computerChoice == 's' and userChoice == 'p'):
        return print("The computer won :(")
    return print("It's a tie!")

rockPaperScissors()