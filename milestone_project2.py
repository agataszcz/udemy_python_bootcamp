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
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        full_deck='' #again,empty STRING! He wants to see every card on a new line, hence "\n'. 
        for card in self.deck:
            full_deck = full_deck+ '\n'+ card.__str__() # add each Card object's print string.He is calling the method.
        return 'The deck has:' + full_deck
       
    def shuffle(self):
        random.shuffle(self.deck) #No need to see the shuffled deck, so no return.Shuffling occurs in place.
        
    def distribute(self):
        received_card= self.deck.pop() #He used the pop() to grab and remove the last item in the list.
        return received_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card): #add card to the list and then add the card's value to the total
        self.cards.append(card)
        self.value = self. value + values[card.rank] #using rank for extracting its value from the dictionary.
        #lowercase to indicate instance, not entire class.
        
        #track aces
        if card.rank=="Ace":
            self.aces += 1 #increase the acount by 1.
        
    
    def adjust_for_ace(self):
        while self.value> 21 and self.aces:     #this means self.aces>0. If my total is greater than 21.
            self.value -=10 #reducing sum by 10, so that Ace=1
            self.aces -= 1 #self.aces=self.aces-1 because an ace becomes a 1.

class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0 #bet amount.
        
    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total=self.total - self.bet

def take_bet(chips): #i should use an argument. Note I am betting chips.
                    #chips.bet and chips.total refer to Chips class.
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet?"))
        except: 
            print("Sorry. Please use an integer.") #in case they did not input a number.
        else:
            if chips.bet>chips.total:
                print("Insufficient chips. You have {} chips".format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.distribute()) #OR: extra_card= deck.distribute(),hand.add_card(extra_card). This adds a line.
    hand.adjust_for_ace()


def hit_or_stand(deck,hand): #I added my touches--break in the middle and continue).
    #Since dealer cannot "stand", this function only applies to player.
    global playing # to control an upcoming while loop
    while True:
        answer=input("Would you like to hit (receive an extra card)? Yes or No? ") #No means player stands.
        
        if answer.lower().startswith('y'):
            hit(deck, hand)
        elif answer.lower().startswith('n'):
            print("Player wishes to stand")
            break
        else: #wrong input.
            print("Wrong input. Would you like to hit? Enter 'yes' or 'no'.")
            continue
        break

def show_some(player,dealer):
    print("Dealer's Hand: ", "|<card hidden>|", dealer.cards[1]) #AS: Dealer has two cards because she does not yet hit.
    print("Player's Hand: ", *player.cards, sep='|')
    
def show_all(player,dealer):
    print("Dealer's Hand: ", *dealer.cards, sep='|')
    print("Dealer's Hand = ",dealer.value)
    print("Player's Hand: ", *player.cards, sep='|')
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
    #Note. He did not double chips. Since computer does not bet, no need to keep track of its chips.
    
def dealer_wins(dealer, player, chips):
    print("Dealer wins. Closer to 21 than Player.")
    chips.lose_bet() 
    
def push(dealer, player):
    print("Dealer and Player tie! This is a push")

#from IPython.display import clear_output



while True:
        # Print an opening statement
    print("Welcome to Blackjack! You win when you are closer to 21 than the Dealer. If you go over 21, you loose.")
    #clear_output()
        # Create an instance of the deck and shuffle it. Do not define the class again.
    mydeck = Deck()
    mydeck.shuffle()
    playing = True
    
    player = Hand() # creating player and dealing 2 cards
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
    
    player_chips = Chips() #Set up the Player's chips. Default value is 100.
    
    show_some(player,dealer)    #Show cards (one dealer card hidden)
    
    take_bet(player_chips)  #Prompt the Player for their bet
        
    #print("while playing", playing)
    while playing: # recall this variable from our hit_or_stand function. This means player's playing. 
        # We switch to dealer when player choses to stand. This sets playing to False and breaks out of the loop.
        #print("call hit or stand")
        hit_or_stand(mydeck, player)  # Prompt for Player to Hit or Stand.
        
        show_some(player,dealer)# Show cards (Dealer does not yet hit, so she has two cards. One is hidden.)
        
        if player.value>21:  # If player's hand exceeds 21, run player_busts() and break out of loop.
            player_busts(dealer, player, player_chips)
            show_all(player,dealer)
            break
            
    #print("while done")
    
    show_all(player,dealer)
    if player.value==21:     #This is a win so dealer no longer collects cards until 17.
        if dealer.value==21:
            print("Dealer and Player have Blackjack")#tie
            push(dealer,player)
        else:           
            player_wins(dealer, player, player_chips)
            
    if player.value<21: # If Player hasn't busted, play Dealer's hand until Dealer reaches 17.
                        #Indentation is different to ensure that my while loop for dealer will execute. 
                        #We cannot check for win P=21 because dealer still has to collect cards until 17.
        while dealer.value<17:
            hit(mydeck, dealer) #Not adding continue because we still need to check for ties or wins.
            show_all(player,dealer)
            
        if dealer.value==21:
            dealer_wins(dealer, player, player_chips)
            
        elif dealer.value>21:
            dealer_busts(dealer, player, player_chips)
            
        elif 17<=dealer.value<21:
                                            # Run different winning scenarios and show all cards
            if dealer.value>player.value:
                dealer_wins(dealer, player, player_chips)
            
            elif dealer.value<player.value:
                player_wins(dealer, player, player_chips)
                                
            elif dealer.value == player.value: #tie
                push(dealer,player)
             
    print('Player has {} chips'.format(player_chips.total))  # Inform Player of their chips total 

    answer=input("Would you like to play again? Yes or No? ") # Ask to play again
    if answer[0].lower()=="y":
        playing = True
        continue
    else:
        print("Exiting Blackjack")
        break        
