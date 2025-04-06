# Project of Rock, Paper, Scissor Game
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("\nWelcome to 'Rock-Paper-Scissor' Game.\n")


game_images = [rock,paper,scissor]
game_items = ['Rock','Paper','Scissor']
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose?\n""Type "
                    "'0' for Rock,"
                    " '1' for Paper,"
                    " '2' for Scissor : "))
if 0 <= user_choice <= 2:
    print(f"\nYou Choose : {game_items[user_choice]}{game_images[user_choice]}")
    print(f"Computer Choose : {game_items[computer_choice]} {game_images[computer_choice]}")

if user_choice >2 or user_choice<0:
    print("You typed an invalid number. You Lose!")
elif computer_choice == user_choice:
    print("Attention, It's a Draw!")
elif computer_choice == 0 and user_choice == 2:
    print("Oops, You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Congrats, You Win!")
elif computer_choice > user_choice :
    print("Oops, You Lose!")
else :
    print("Congrats, You Win!")   # elif computer_choice < user_choice :  print("Congrats, You Win!")
















