from replit import clear
#You can call clear() to clear the output in the console.

from art2 import logo

print(logo)

auction_dictionary = {}


def find_highest(bid_record):
    higher_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > higher_bid:
            higher_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_record[winner]}")


print("Welcome to the secret auction program!")

continue_auction = False

while not continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dictionary[name] = bid

    play = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if play == 'no':
        continue_auction = True
        find_highest(auction_dictionary)
    elif play == 'yes':
        clear()
