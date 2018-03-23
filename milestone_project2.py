#!/usr/bin/env python3
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)


class Deck:
    
    def __init__(self):
        self.deck = []  #start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        full_deck='' #must use a string (not a list) because __str__() returns a string repr, not a list (type error).
        			#We could not concatenate a string repr to a list (error).  
        for card in self.deck:
            full_deck = full_deck+ '\n'+ card.__str__() # add each Card object's string repr (calling the object's method).
        return 'The deck has:' + full_deck
       
    def shuffle(self):
        random.shuffle(self.deck) #No need to see the shuffled deck, so no return. Shuffling occurs in place.
        
    def distribute(self):
        received_card = self.deck.pop() #to grab and remove the last item in the list.
        return received_card

class Hand:
#Hand shows the value of cards in the player's hand and the dealer's hand.
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #add an attribute to keep track of aces.
    
    def add_card(self,card): #add card to the list and then add the card's value to the total
        self.cards.append(card)
        self.value = self. value + values[card.rank] #using rank to extract its value from the dictionary.
        											#lowercase to indicate an instance, not the entire class.
        
        #to track aces
        if card.rank=="Ace":
            self.aces += 1 #increase the count by 1.
        
    
    def adjust_for_ace(self):
        while self.value> 21 and self.aces:     #this means self.aces>0. If my total is greater than 21:
            self.value -=10 #reducing sum by 10, so that Ace=1
            self.aces -= 1 #reduce the count of aces: self.aces=self.aces-1 because an ace became a 1.

class Chips:
#Chips only keeps track of the player's chips. The dealer never bets.
    
    def __init__(self, total=100):
        self.total = total  #set to a default value.
        self.bet = 0 #number of chips that the player bets.
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet

def take_bet(chips): 
                    #chips.bet and chips.total refer to Chips class.
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except: 
            print("Sorry. Please use an integer.") #in case they did not input a number.
        else:
            if chips.bet>chips.total:
                print("Insufficient chips. You have {} chips".format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.distribute()) #OR: extra_card = deck.distribute(),hand.add_card(extra_card).
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    #Since the dealer cannot "stand", this function only applies to the player.
    global playing # to control an upcoming while loop
    while True:
        answer = input("Would you like to hit (receive an extra card)? Yes or No? ") #'No' means player stands.
        
        if answer.lower().startswith('y'):
            hit(deck, hand)
        elif answer.lower().startswith('n'):
            print("Player wishes to stand")
            playing = False
            break
        else: #wrong input.
            print("Wrong input. Would you like to hit? Enter 'yes' or 'no'.")
            continue
        break

def show_some(player,dealer): #to display cards
    print("\nDealer's Hand: ", "\n<card hidden>\n", dealer.cards[1]) #Dealer has two cards because she does not yet hit.
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    
def show_all(player,dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n')
    print("Dealer's Hand = ",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand = ",player.value)

def player_busts(dealer, player, chips):                     
    print("Player busted. Dealer wins!")
    chips.lose_bet() #losing chips
        

def player_wins(dealer, player, chips): 
    print("Player wins. Closer to 21 than Dealer.")
    chips.win_bet() #adding chips
        
    
def dealer_busts(dealer, player, chips):
    print("Dealer busted. Player wins!")
    chips.win_bet()
    #The player gains chips. We are not keeping track of the dealer's wins.
    
def dealer_wins(dealer, player, chips):
    print("Dealer wins. Closer to 21 than Player.")
    chips.lose_bet() 
    
def push(dealer, player):
    print("Dealer and Player tie! This is a push")

from IPython.display import clear_output #to remove history of the game



while True:
        # Print an opening statement
    print("\nWelcome to Blackjack! You win when you have Blackjack (21) or are closer to 21 than the Dealer. If you go over 21, you loose.")
    clear_output()
        # Create an instance of the deck and shuffle it.
    mydeck = Deck()
    mydeck.shuffle()
    playing = True
    
    player = Hand() #creating player and dealing 2 cards
    player.value = 0
    player.cards = []
    
    received_card1 = mydeck.distribute()
    player.add_card(received_card1)
    player.adjust_for_ace()
    
    received_card2 = mydeck.distribute()
    player.add_card(received_card2)
    player.adjust_for_ace()
    
    dealer = Hand()  #creating dealer and distributing 2 cards
    dealer.value = 0
    dealer.cards = []
    
    dealer.add_card(mydeck.distribute())
    dealer.adjust_for_ace()
    
    dealer.add_card(mydeck.distribute())
    dealer.adjust_for_ace()
    
    player_chips = Chips() #Player's chips. Default value is 100.
    
    show_some(player,dealer)    #Show cards (one dealer card hidden)
    
    take_bet(player_chips)  #asking the player to bet
        
    #testing: print("while playing", playing)
    while playing: # We need this to run hit_or_stand. This means player's playing. 
        # Switch to the dealer when player choses to stand. This sets playing to False and breaks out of the loop.
        #testing:print("call hit or stand")
        hit_or_stand(mydeck, player)  #Asking the player to Hit or Stand.
        
        show_some(player,dealer)# Show cards. Dealer does not yet hit, so she has two cards. One card is hidden.)
        
        if player.value>21:  # If player's hand exceeds 21, he busts. We break out of loop.
            player_busts(dealer, player, player_chips)
            break
            
    #testing: print("while done")
    
    show_all(player,dealer) #showing all cards once the player has decided to stand.

    if player.value==21:     #This is an immediate win so the dealer does not collect any cards.
        if dealer.value==21:
            print("Dealer and Player have Blackjack") #tie
            push(dealer,player)
        else:           
            player_wins(dealer, player, player_chips)
            
    if player.value<21: #If the player hasn't busted, the dealer hits until she reaches 17.
                        
        while dealer.value<17:  #Increased indentation because the while loop should execute only when the player has less than 21. 
            hit(mydeck, dealer)
            show_all(player,dealer)
            #To print individual cards: extra_card = mydeck.distribute(), print(extra_card), dealer.add_card(extra_card), dealer.adjust_for_ace()
            
        if dealer.value==21:      # Running different winning scenarios.
            dealer_wins(dealer, player, player_chips)
            
        elif dealer.value>21:
            dealer_busts(dealer, player, player_chips)
            
        elif 17<=dealer.value<21:

            if dealer.value>player.value:
                dealer_wins(dealer, player, player_chips)
            
            elif dealer.value<player.value:
                player_wins(dealer, player, player_chips)
                                
            elif dealer.value == player.value: #tie
                push(dealer,player)
             
    print('Player has {} chips'.format(player_chips.total))  # Informing the player of his/her chips total 

    answer=input("Would you like to play again? Yes or No? ") # Asking to play again
    if answer[0].lower()=="y":
        playing = True
        continue
    else:
        print("Exiting Blackjack")
        break        