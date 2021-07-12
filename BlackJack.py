import random
import db as money
import sys

def createDeck():
    #Creates and returns a deck of cards
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

def dealPlayerCard(deck, playerCards):
    #deals a single card to player. If Ace is drawn, player is given option to
    #choose between 1 and 11. If Ace = 11 causes player to bust, 1 is
    #automatically chosen. 

    card = random.choice(deck)
    deck.remove(card)
    suit = card[0]
    rank = card[1]
    value = card[2]
    value2 = int(card[2])
    value3 = 0
    value3 += value2
    singleCard = (suit, rank, value3)

    playerPoints = 0
    for card in playerCards:
        amount = int(card[2])
        playerPoints += amount
    
    if value3 == 11:
        value1 = playerPoints + value3
        if value1 > 21:
            value3 = 1
            print("Ace = 1")
        elif value1 <= 21:
            value3 = 11
            ("Ace = 11")
        playerCards.append(singleCard)
    else:
        playerCards.append(singleCard)
    return playerCards

def showPlayerHand(playerCards):
    #show current player hand
    for card in playerCards:
        suit = card[0]
        rank = card[1]
        print(str(rank) + " of " + str(suit))

def dealDealerCard(deck, dealerCards):
    #deals single card to dealer
    card = random.choice(deck)
    deck.remove(card)
    suit = card[0]
    rank = card[1]
    value = card[2]
    singleCard = (suit, rank, value)
    dealerCards.append(singleCard)
    return dealerCards

def showDealerHand(dealerCards):
    #show dealer current hand
    for card in dealerCards:
        suit = card[0]
        rank = card[1]
        print(str(rank) + " of " + str(suit))

def determinePlayerPoints(playerCards):
    #calculate current player points. 
    playerPoints = 0
    for card in playerCards:
        amount = int(card[2])
        playerPoints += amount
    return playerPoints

def determineDealerPoints(dealerCards, deck):
    #calculate current dealer points.
    #if dealer points are < 17, 3rd card is automatically dealt. 
    dealerPoints = 0
    for card in dealerCards:
        amount = int(card[2])
        dealerPoints += amount

    if dealerPoints < 17:
        card = random.choice(deck)
        deck.remove(card)
        suit = card[0]
        rank = card[1]
        value = card[2]
        singleCard = (suit, rank, value)
        dealerCards.append(singleCard)
        return dealerCards
            
    
def determineWinner(playerCards, dealerCards, betAmount):
    #imports player money .txt file
    #Calc current points and determine winner.
    #Add/Subtract bet based on winner. 
    money.read_player_money()
    player_money = money.read_player_money()
    total = "0"
    for value in player_money:
        total += str(value)
    total = round(float(total), 2)

    
    playerPoints = 0
    for card in playerCards:
        amount = int(card[2])
        playerPoints += amount
    print("\nYOUR POINTS: \t" + str(playerPoints))

    dealerPoints = 0
    for card in dealerCards:
        amount = int(card[2])
        dealerPoints += amount
    print("DEALER POINTS: \t" + str(dealerPoints))
    
    
    if (playerPoints > 21 and dealerPoints > 21):
        print("\nNo winner")
        print("Money: $" + str(total))
    
    elif (playerPoints > 21 and dealerPoints <= 21):
        print("\nDealer wins")
        #losings = []
        losings = (betAmount * 1.5)
        newTotal = round(total - (losings), 2)
        money.write_player_money(newTotal)
        print("Money: $" + str(newTotal))
        
    elif (playerPoints <= 21 and dealerPoints > 21):
        print("\nPlayer wins")
        #winnings = []
        winnings = betAmount * 1.5
        newTotal = round(total + (winnings), 2)
        money.write_player_money(newTotal)
        print("Money: $" + str(newTotal))
        #player wins
        
    elif (playerPoints <= 21 and dealerPoints <= 21):
        if (playerPoints > dealerPoints):
            print("\nPlayer wins")
            #winnings = []
            winnings = betAmount * 1.5
            newTotal = round(total + (winnings), 2)
            money.write_player_money(newTotal)
            print("Money: $" + str(newTotal))
            #player wins
            
        elif (playerPoints < dealerPoints):
            print("\nDealer wins")
            #losings = []
            losings = (betAmount * 1.5)
            newTotal = round(total - (losings), 2)
            money.write_player_money(newTotal)
            print("Money: $" + str(newTotal))
            #dealer wins
            
        elif (playerPoints == dealerPoints):
            print("\nTie game")
            print("Money: $" + str(total))
            #tie / no winner
            
    
def shuffle_deck(deck):
    #shuffles the deck
    random.shuffle(deck)
    print("The deck has been shuffled\n")

def display():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def bet():
    #import player money .txt file
    #completes data validation on bet. 
    #If player money is < 5 it will ask player if they would like more money added to account.
    money.read_player_money()
    player_money = money.read_player_money()
    total = "0"
    for value in player_money:
        total += str(value)
    total = round(float(total), 2)
    print("Money: $" + str(total))
    while True:
        try:
            betAmount = float(input("Bet amount: $"))
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
        elif betAmount <= total:
            if betAmount >= 5 and betAmount <=1000:    
                return betAmount
            else:
                print("Please enter a bet between 5 and 1000!")
                continue
        else:
            print("You can not bet more than you have in your account.")
            continue
        
        
    
def main():
    display()
    deck = createDeck()
    #player_money = get_player_money()

    choice = "y"
    while choice.lower() == "y":
        playerCards = []
        dealerCards = []


        #shuffle_deck(deck)
        playerPoints = determinePlayerPoints(playerCards)
        betAmount = bet()
        print("\nDEALER'S SHOW CARD: ")
        dealDealerCard(deck, dealerCards)
        showDealerHand(dealerCards)
        dealDealerCard(deck, dealerCards)

        print("\nYOUR CARDS: ")
        dealPlayerCard(deck, playerCards)
        dealPlayerCard(deck, playerCards)
        showPlayerHand(playerCards)


        while (True):
            hitOrStand = input("\nHit or stand? (hit/stand): ")
            if hitOrStand.lower() == "hit":
                dealPlayerCard(deck, playerCards)
                print("\nYOUR CARDS: ")
                showPlayerHand(playerCards)
                playerPoints = determinePlayerPoints(playerCards)
                if playerPoints > 21:
                    print("\nBUST!")
                    break
                else:
                    continue
                break
                
            elif hitOrStand.lower() == "stand":
                print("\nDEALER'S CARDS")
                determineDealerPoints(dealerCards, deck)
                showDealerHand(dealerCards)
                break
            else:
                print("Please enter 'hit' or 'stand'. Try Again. ")
                continue

        determineWinner(playerCards, dealerCards, betAmount)
        
        choice = input("\nWould you like to play again? (y/n): ")
    print("\nCome back soon!")
    print("Bye!")
    
    
if __name__== "__main__":
    main()
