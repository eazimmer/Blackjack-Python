import random

def calculateScore(cards):
    score = 0
    hasAce = False

    for card in cards:
        try:
            score += int(card)
        except:
            if card == "A":
                hasAce = True
            else:
                score += 10

    if hasAce:
        if (score + 11) > 21:
            score += 1
        else:
            score += 11

    return score


def printStatus(playerCards, dealerCards):
    print("\n")
    print("Player's total is " + str(calculateScore(playerCards)) + ":\n")
    
    for card in playerCards:
        print(card + ", ")
    print("\n")

    print("Dealer's total is " + str(calculateScore(dealerCards)) + ":\n")
    for card in dealerCards:
        print(card + ", ")
    print("\n")
    
    

def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    playerCards = []
    dealerCards = []
    
    random.shuffle(deck)

    print("Dealer draws first card.\n")
    dealerCards.append(deck.pop())
    
    print("Player receives two cards.\n")
    playerCards.append(deck.pop())
    dealerCards.append(deck.pop())
    
    printStatus(playerCards, dealerCards)

    while True:
        selection = input("Do you want to (H)it, (S)tay, or (Q)uit?\n").upper()

        if selection == "H":
            playerCards.append(deck.pop())
            printStatus(playerCards, dealerCards)

            if (calculateScore(playerCards) > 21):
                print("You busted! You lose!\n")
                return

        elif selection == "S":
            break

        elif selection == "Q":
            return

    print("Dealer draws rest of cards.\n")
    while (calculateScore(dealerCards) < 17):
        dealerCards.append(deck.pop())
        
    printStatus(playerCards, dealerCards)

    if (calculateScore(dealerCards) > 21):
        print("Dealer busts! You win!\n")
        
    elif (calculateScore(dealerCards) > calculateScore(playerCards)):
        print("Dealer wins!\n")
        
    elif (calculateScore(dealerCards) < calculateScore(playerCards)):
        print("You win!\n")
        
    else:
        print("It's a tie!\n")

    return
    
    
