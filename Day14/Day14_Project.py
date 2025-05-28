import art
from Dataset import data
import random
def format_data(account):

    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, From {country}."
def check_answer(guess,a_follower, b_follower):
    if a_follower>b_follower:
        return guess=="a"
    else:
        return guess=="b"
score = 0

print("Welcome to Higher Lower Game.")
print(art.logo)
print("\n"*10)

repeat = True
while repeat is True:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")
    print(f"Your Current Score: {score}")

    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    account_a_follower = account_a["follower"]
    account_b_follower = account_b["follower"]

    is_correct = check_answer(guess,account_a_follower,account_b_follower)

    if is_correct:
        score+=1
        print(f"You're Right. Current score {score}")
    else:
        print(f"Sorry, that's Wrong. Final score: {score}")
        break

