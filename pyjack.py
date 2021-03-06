#!/usr/bin/python3

#Chris Moser 03/05/2014

#Probably have to start with a deck

import random

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        long_rank = {"A":"Ace", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine", "10":"Ten", "J":"Jack", "Q":"Queen", "K":"King"}
        long_suit = {"D":"Diamonds", "H":"Hearts", "C":"Clubs", "S":"Spades"}
        return long_rank[self.rank] + " of " + long_suit[self.suit]

    def __repr__(self):
        return self.rank + self.suit

class Deck(object):
    def __init__(self):
        self.cards = []

        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["D", "H", "C", "S"]

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        cards_str = ""
        for card in self.cards:
            cards_str += str(card) + "\n"
        return cards_str

    def __repr__(self):
        cards_repr = ""
        for card in self.cards:
            cards_repr += repr(card) + " "
        return cards_repr

    def shuffle(self):
        return random.shuffle(self.cards)
    
    def deal(self, num_cards):
        new_hand = []
        for cards in range(num_cards):
            new_hand.append(self.cards.pop())
        return new_hand

class Hand(object):
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        cards_str = ""
        for card in self.cards:
            cards_str += str(card) + "\n"
        return cards_str

    def __repr__(self):
        cards_repr = ""
        for card in self.cards:
            cards_repr += repr(card) + " "
        return cards_repr




myDeck = Deck()
myDeck.shuffle()

print(repr(myDeck))

dealerHand = myDeck.deal(2)
myHand = myDeck.deal(2)

print(dealerHand)
print(repr(dealerHand))


print(myHand)
print(repr(myHand))


