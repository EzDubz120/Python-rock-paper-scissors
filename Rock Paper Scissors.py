import random
import time

print("Welcome to rock paper scissors")
time.sleep(1)

player_choice = input("Enter Rock, Paper or scissors ")
computer_choice = random.randint(1,3)

if computer_choice == 1 and player_choice == "rock":
    print("The computer chose rock so you draw")

elif computer_choice == 1 and player_choice == "scissors":
    print("The computer chose rock so you lose")

elif computer_choice == 1 and player_choice == "paper":
    print("The computer chose rock so you win")


elif computer_choice == 2 and player_choice == "paper":
    print("The computer chose paper so you draw")

elif computer_choice == 2 and player_choice == "rock":
    print("The computer chose paper so you lose")

elif computer_choice == 2 and player_choice == "scissors":
    print("The computer chose paper so you win")


elif computer_choice == 3 and player_choice == "scissors":
    print("The computer chose scissors so you draw")

elif computer_choice == 3 and player_choice == "rock":
    print("The computer chose scissors so you win")

elif computer_choice == 3 and player_choice == "paper":
    print("The computer chose scissors so you lose")


