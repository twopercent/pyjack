#!/usr/bin/python3

#Chris Moser 03/05/2014

#Probably have to start with a deck

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank




class Deck(object):
    def __init__(self):
        self.name = name



print ("Hello World!")

myCard = Card("hearts", "7")
hollysCard = Card("diamonds", "ace")

print("Hollys card is the " + hollysCard.rank + " of " + hollysCard.suit)
