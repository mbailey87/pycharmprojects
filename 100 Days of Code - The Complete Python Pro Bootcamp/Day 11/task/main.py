import random
import art

hit = True
print(art.logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def ace_to_one(hand):
    if 11 in hand and sum(hand) > 21:
        for i in reversed(range(len(hand))):
            if hand[i] == 11:
                hand[i] = 1
                break
    return hand

def calc_totals(cards):
    ace_to_one(cards)
    total = sum(cards)
    return total

def another_game():
    global hit
    while hit:
        play_again = input("do you want to play again type y for yes and n for no\n").lower()
        if play_again == 'y':
            play_game()
        elif play_again == 'n':
            hit = False
            return hit
        else:
            print("please pick a valid entry")

def play_game():
    players_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    dealer_shown_cards = [dealer_cards[0]]
    calc_totals(players_cards) and calc_totals(dealer_cards)
    def print_scores():
        print ("Player: ", players_cards, calc_totals(players_cards))
        print("Dealer: ",dealer_shown_cards)
    print_scores()
    # lose conditions
    def compare(player, dealer):
        if calc_totals(dealer) < calc_totals(player) or calc_totals(dealer) > 21:
            print("You Win")
        if calc_totals(player) < calc_totals(dealer) and calc_totals(dealer_cards) <= 21 or calc_totals(player) > 21:
            print(f"You Lose.")
        if calc_totals(player) == calc_totals(dealer):
            print("Draw")
        another_game()

    while hit:
        if calc_totals(players_cards) > 21:
            print(f"You Lose.")
            another_game()
        if calc_totals(players_cards) == 21:
            print("You Win")
            another_game()
        take_hit = input(f"your total is {calc_totals(players_cards)}\nthe dealers current total is {calc_totals(dealer_shown_cards)}\ndo you want to hit type 'y' for yes and 'n' for no\n").lower()
        if take_hit == 'y':
            new_card_player = deal_card()
            players_cards.append(new_card_player)
            calc_totals(players_cards)
            print_scores()

        if take_hit == "n":
            calc_totals(players_cards) and calc_totals(dealer_cards)
            while calc_totals(dealer_cards) < 17:
                dealer_cards.append(deal_card())
                calc_totals(dealer_cards)
            print("Player: ", players_cards, calc_totals(players_cards))
            print("Dealer: ", dealer_cards)
            compare(players_cards, dealer_cards)

play_game()