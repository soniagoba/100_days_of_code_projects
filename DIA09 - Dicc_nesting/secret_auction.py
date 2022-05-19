print("Welcome to the secret auction program")

biders = {}
other_bidder = "yes"
while other_bidder == "yes":
    #Se limpia pantalla
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    biders[name] = bid
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

highest_bid = 0
for key, value in biders.items():
    if biders[key] >= highest_bid:
        highest_bid = biders[key]
    else:
        pass
#METHOD 1:
""" biders_key_list = list(biders.keys())
biders_value_list = list(biders.values())
position_highest_bid = biders_value_list.index(highest_bid)
winner = biders_key_list[position_highest_bid] """

#METHOD 2
for key, value in biders.items():
    if highest_bid == value:
        winner = key

print(f"The winner is {winner} with a bid of {highest_bid}€")

