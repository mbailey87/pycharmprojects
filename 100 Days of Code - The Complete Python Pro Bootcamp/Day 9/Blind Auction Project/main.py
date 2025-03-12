# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import os
import art

bidders = {}
next_bidder = True

print(art.logo)

while next_bidder:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    bidders[name] = bid
    is_other_bidder = input("is there another bidder 'yes' or 'no' \n").lower()
    if is_other_bidder == 'no':
        print('thank you')
        print('\n' * 100)
        break
    elif is_other_bidder == 'yes':
        print('\n' * 100)
        continue
    else:
        print('enter a valid option')

bid = 0
for person in bidders:
    if bidders[person] > bid:
        bid = bidders[person]
bidder = next(name for name, value in bidders.items() if value == bid)

print(f'The winner is {bidder} with a bid of ${bid}')