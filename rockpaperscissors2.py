# enums,user inputs,loops
from enum import Enum
import sys
import random

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

playagain = True

while playagain:

    playerChoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("Invalid NUmber---try 1,2,3")

    computerchoice = random.choice("123")
    terminal = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Terminal chose " + str(RPS(terminal)).replace('RPS.', '').title() + ".\n")


    if player == 1 and terminal == 3:
        print("You Win:)")
    elif terminal == 1 and player == 2:
        print("You Win:)")
    elif terminal == 2 and player == 3:
        print("You Win:)")
    elif terminal == player:
        print("Tie Game!!")
    else:
        print("Terminal Wins!!\tYou lost")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")


