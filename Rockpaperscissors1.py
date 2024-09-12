# enums,user inputs
from enum import Enum
import sys
import random

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

print("")
playerChoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("Invalid NUmber---try 1,2,3")

computerchoice = random.choice("123")
terminal = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Terminal chose " + str(RPS(terminal)).replace('RPS.', '') + ".")
print("")

if player == 1 and terminal == 3:
    print("You Win:)")
elif terminal == 1 and player == 2:
    print("You Win:)")
elif terminal == 2 and player == 3:
    print("You Win:)")
else:
    print("Terminal Wins!!\tYou lost")

