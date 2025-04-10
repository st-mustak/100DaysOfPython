from art import logo

def highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe Winner is {bidder} with the bid of ₹ {bid_amount}")

print(logo)
all_bids = {}
more_bid = 'y'
while more_bid == 'y':
    name = input("\nEnter Your Name: ")
    bid_price = int(input("Enter Your Bid Amount: ₹ "))
    all_bids[name] = bid_price

    more_bid = input("\nAre there any other bidder? "
                     "Type 'y' for Yes and 'n' for No : ")
    if more_bid=='y':
        print("\n"*50)


highest_bidder(all_bids)
