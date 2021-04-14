#Import module and define variables

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 0, "Queen": 10, "King": 10, "Ace": 11}

playing = True

# Classes

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + "of " + self.suit
    
class Deck: #creates a deck of cards
    
    def __init__(self):
        self.deck = [] #Empty list because we have not made an empty deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __string__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand: #Show all the cards that the dealer and the player have
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #Keep track of aces
        
    def add_card(self, card): # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing
    
    while True:
        ask = input("would you like to hit or stand? Please enter 'H' or 'S': ").upper
        
        if ask == "H":
            hit(deck,hand)
        
        elif ask == "S":
            print("Player stands, Dealer is playing")
            playing = False
        
        else:
            print("Sorry I did not understand that! Please try again!")
            continue
        break
        
def show_some(player, dealer):
    print("\nDealer's hand: ")
    print(" <card hidden>")
    print(" ", dealer.cards[1])
    print("\nPlayer's hand: ", + player.cards, sep="\n ")
    
def show_all(player, dealer):
    print("\nDealer's hand: ", + dealer.cards, sep="\n ")
    print("Dealer's hand =", dealer.value)
    print("\nPlayer's hand: ", + player.cards, sep="\n ")
    print("Player's hand =", players.value)
    
    
    
def player_busts(player, dealer):
    print("PLAYER BUSTS!")
    
def player_wins(player, dealer):
    print("PLAYER WINS")
    
    
def dealer_busts(player, dealer):
    print("DEALER BUSTS!")
    
def dealer_wins(player, dealer):
    print("DEALER WINS")
    
def push(player, dealer):
    print("It's a push! Player and Dealer tie!")
    
while True:
    print("Welcome to BlackJack")
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    while playing:
        
        hit_or_stand(deck, [player_hand])
        show_some(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break
        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)
            
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            
    Print("\nPlayer's winnings stand at", + player_chips.total)
    
    new_game = input("Would you like to play a new game? Enter 'Y' or 'N': ").lower
    if new_game == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
        
    