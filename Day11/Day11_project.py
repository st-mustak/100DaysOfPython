import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw!"
    elif c_score ==0:
        return "You Lose, Opponent has Blackjack."
    elif u_score==0:
        return "Congrats! You wins with Blackjack."
    elif u_score>21:
        return "Loose, You Over."
    elif c_score>21:
        return "Win, Computer Over."
    elif u_score>c_score:
        return "You Win!"
    else:
        return "You Lose."

def playgame():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards} , Current Score: {user_score}")
        print(f"Computer First Card: {computer_cards[0]} , Current Score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ") == "y":
    playgame()