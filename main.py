from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

bid = {}
repeat = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner=""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        bid_amount = int(amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while repeat:
    name = input("What is your name?:")
    price = input("How much would you like to bid: $")
    rep = input("Are there other bidder? Type 'yes' or 'no'")

    
    bid[name] = price

    if (rep == "yes"):
        clear()
    else:
        find_highest_bidder(bid)
        repeat = False
        