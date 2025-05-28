#Guessing number
import art
EASY_LEVEL=10
HARD_LEVEL = 5
from random import randint

def check_number(guesses, answers, turn):
    if guesses < answers:
        print("Too Low.Try Higher.")
        return turn - 1
    elif guesses > answers:
        print("Too High. Try Lower.")
        return turn - 1
    else:
        print(f"Congrats! You've Got it.The number is {guesses}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'hard' or 'easy': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game.")
    print("I'm guessing a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()

    guess =0
    while guess!=answer:
        print(f"You have {turns} attempts left.")
        guess = int(input("Make a Guess:"))
        turns = check_number(guess,answer,turns)
        if turns ==0:
            print("Lose, You've runs out of turns.Try again.")
            return

game()