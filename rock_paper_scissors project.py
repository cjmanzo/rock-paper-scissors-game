import random

myScore = 0
computerScore = 0

while True:
    """
    User is asked to enter input from the given selection.
    Then follows by an option for quitting
    """
    userInput = input("Enter rock, paper, or scissors: ").lower()
    if userInput == "quit":
        print ("I resign! Game Over")
        break
    if userInput != "rock" and userInput != "paper" and userInput != "scissors":
        print("Please choose a correct input\n")
        continue

    """
    Computer imput is generated through getting a random choice from the same selection.
    """
    computerInput = random.choice(["rock", "paper", "scissors"])
    print (f"Computer: {computerInput}\n")


    """
    Deciding factor and incrementing score
    """
    if computerInput == userInput:
        print ("It's a tie!")
    elif userInput == "rock" and computerInput == "scissors":
        print ("You Win!")
        myScore += 1
    elif userInput == "scissors" and computerInput == "paper":
        print ("You Win!")
        myScore += 1
    elif userInput == "paper" and computerInput == "rock":
        print ("You Win!")
        myScore += 1
    else:
        print ("You Lost!")
        computerScore += 1

    """
    Outcome, Game over whoever reaches 5 first.
    """
    print(f"my score: {myScore} computer score: {computerScore}\n\n")
    if myScore == 5 or computerScore == 5:
        print("Game Over!")
        break












