import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_total(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_state(player_hand, dealer_hand, reveal_dealer=False):
    player_total = calculate_total(player_hand)
    if reveal_dealer:
        dealer_total = calculate_total(dealer_hand)
        print(f"Dealer's Cards: {dealer_hand} = {dealer_total}")
    else:
        print(f"Dealer's Shown Cards: [{dealer_hand[0]}, X]")
    print(f"Your Cards: {player_hand} = {player_total}")

def play_round():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    display_state(player_hand, dealer_hand, reveal_dealer=False)

    while True:
        player_total = calculate_total(player_hand)

        if player_total > 21:
            print("You busted! Dealer wins.")
            return

        choice = input("Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card())
            display_state(player_hand, dealer_hand, reveal_dealer=False)
        else:
            break  # player stands

    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    display_state(player_hand, dealer_hand, reveal_dealer=True)

    if dealer_total > 21:
        print("Dealer busts! You win.")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a draw!")

def start_game():
    print("Welcome to the Blackjack Game!")
    while True:
        play_round()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

start_game()
