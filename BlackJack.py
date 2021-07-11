import random
import db as money
import sys

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = []

    for suit in suits:
        counter = 0
        for rank in ranks:
            card = []
            card.append(suit)
            card.append(rank)
            card.append(values[counter])
            deck.append(card)
            counter += 1
    return deck

def deal_player_card(deck, player_cards):
    #Figure out how to pop random choice off lists

    card = random.choice(deck)
    deck.remove(card)
    suit = card[0]
    rank = card[1]
    value = card[2]
    value2 = int(card[2])
    value3 = 0
    value3 += value2
    single_card = (suit, rank, value3)

    player_points = 0
    for card in player_cards:
        amount = int(card[2])
        player_points += amount
    
    if value3 == 11:
        value1 = player_points + value3
        if value1 > 21:
            value3 = 1
            print("Ace = 1")
        elif value1 <= 21:
            value3 = 11
            ("Ace = 11")
        player_cards.append(single_card)
    else:
        player_cards.append(single_card)
    return player_cards

def show_player_hand(player_cards):
    for card in player_cards:
        suit = card[0]
        rank = card[1]
        print(str(rank) + " of " + str(suit))

def deal_dealer_card(deck, dealer_cards):
    card = random.choice(deck)
    deck.remove(card)
    suit = card[0]
    rank = card[1]
    value = card[2]
    single_card = (suit, rank, value)
    dealer_cards.append(single_card)
    return dealer_cards

def show_dealer_hand(dealer_cards):
    for card in dealer_cards:
        suit = card[0]
        rank = card[1]
        print(str(rank) + " of " + str(suit))

def determine_player_pts(player_cards):
    player_points = 0
    for card in player_cards:
        amount = int(card[2])
        player_points += amount
    return player_points

def determine_dealer_pts(dealer_cards, deck):       
    dealer_points = 0
    for card in dealer_cards:
        amount = int(card[2])
        dealer_points += amount

    if dealer_points < 17:
        card = random.choice(deck)
        deck.remove(card)
        suit = card[0]
        rank = card[1]
        value = card[2]
        single_card = (suit, rank, value)
        dealer_cards.append(single_card)
        return dealer_cards
            

#def get_player_money():
#    money.read_player_money()
#    player_money = money.read_player_money()
#    player_money = str(player_money)
#    return player_money
    
def determine_winner(player_cards, dealer_cards, bet_amount):
    money.read_player_money()
    player_money = money.read_player_money()
    total = "0"
    for value in player_money:
        total += str(value)
    total = round(float(total), 2)

    
    player_points = 0
    for card in player_cards:
        amount = int(card[2])
        player_points += amount
    print("\nYOUR POINTS: \t" + str(player_points))

    dealer_points = 0
    for card in dealer_cards:
        amount = int(card[2])
        dealer_points += amount
    print("DEALER POINTS: \t" + str(dealer_points))
    
    
    if (player_points > 21 and dealer_points > 21):
        print("\nNo winner")
        print("Money: $" + str(total))
    
    elif (player_points > 21 and dealer_points <= 21):
        print("\nDealer wins")
        #losings = []
        losings = (bet_amount * 1.5)
        new_total = total - (losings)
        money.write_player_money(new_total)
        print("Money: $" + str(new_total))
        
    elif (player_points <= 21 and dealer_points > 21):
        print("\nPlayer wins")
        #winnings = []
        winnings = bet_amount * 1.5
        new_total = total + (winnings)
        money.write_player_money(new_total)
        print("Money: $" + str(new_total))
        #player wins
        
    elif (player_points <= 21 and dealer_points <= 21):
        if (player_points > dealer_points):
            print("\nPlayer wins")
            #winnings = []
            winnings = bet_amount * 1.5
            new_total = total + (winnings)
            money.write_player_money(new_total)
            print("Money: $" + str(new_total))
            #player wins
            
        elif (player_points < dealer_points):
            print("\nDealer wins")
            #losings = []
            losings = (bet_amount * 1.5)
            new_total = total - (losings)
            money.write_player_money(new_total)
            print("Money: $" + str(new_total))
            #dealer wins
            
        elif (player_points == dealer_points):
            print("\nTie game")
            print("Money: $" + str(total))
            #tie / no winner
            
    
def shuffle_deck(deck):
    random.shuffle(deck)
    print("The deck has been shuffled\n")

def display():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def bet():
    money.read_player_money()
    player_money = money.read_player_money()
    total = "0"
    for value in player_money:
        total += str(value)
    total = float(total)
    print("Money: $" + str(total))
    while True:
        try:
            bet_amount = float(input("Bet amount: $"))
        except ValueError:
            print("Invalid bet amount. Try again \n")
            continue
        if total < 5:
            choice = input("Would you like to add more money to your account? (y/n)")
            if choice.lower() == "y":
                extra_coin = 100
                money.write_player_money(extra_coin)
                print("Adding " + extra_coin + "'s to your account")
            elif choice.lower() == "n":
                print("Well..... okay. Bye!")
                sys.exit()
        elif bet_amount <= total:
            if bet_amount >= 5 and bet_amount <=1000:    
                return bet_amount
            else:
                print("Please enter a bet between 5 and 1000!")
                continue
        else:
            print("You cant bet more than you have")
            continue
        
        
    
def main():
    display()
    deck = create_deck()
    #player_money = get_player_money()

    choice = "y"
    while choice.lower() == "y":
        player_cards = []
        dealer_cards = []


        #shuffle_deck(deck)
        player_points = determine_player_pts(player_cards)
        bet_amount = bet()
        print("\nDEALER'S SHOW CARD: ")
        deal_dealer_card(deck, dealer_cards)
        show_dealer_hand(dealer_cards)
        deal_dealer_card(deck, dealer_cards)

        print("\nYOUR CARDS: ")
        deal_player_card(deck, player_cards)
        deal_player_card(deck, player_cards)
        show_player_hand(player_cards)


        while (True):
            hit_or_stand = input("\nHit or stand? (hit/stand): ")
            if hit_or_stand.lower() == "hit":
                deal_player_card(deck, player_cards)
                print("\nYOUR CARDS: ")
                show_player_hand(player_cards)
                player_points = determine_player_pts(player_cards)
                if player_points > 21:
                    print("\nBUST!")
                    break
                else:
                    continue
                break
                
            elif hit_or_stand.lower() == "stand":
                print("\nDEALER'S CARDS")
                determine_dealer_pts(dealer_cards, deck)
                show_dealer_hand(dealer_cards)
                break

        determine_winner(player_cards, dealer_cards, bet_amount)
        
        choice = input("\nWould you like to play again? (y/n): ")
    print("\nCome back soon!")
    print("Bye!")
    
    
if __name__== "__main__":
    main()
