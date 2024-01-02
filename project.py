#########################################
##### WELCOME TO YOUR OOP PROJECT #######
########################################

# PROJECT.PY
# For this project you will be using OOP to create a card game.
# This card
# game will be the card game "War" for two players, you and the computer.
# if you don't know how to play "War" here are the basic rules:
#
# The deck is divided evenly,with each player receiving 26 cards, dealt one
# at a time,face down.Anyoone may deal first.Each player places his stack of
# cards face down,in front of him.
#
# The play
#
# Each player turns up a card at the same time and the player with higher
# card takes both cards and puts them, face down, on the bottom of his stack
#
# If the cards are  the same ranks, it is war.Each players turns up
# three cards face down and one card face up.The player with the
# higher cards takes both piles (six cards). If the turned-up cards
# are again the same rank, each player places another card face down
# and turns up.The  player with the higher card takes all 10 cards,
# and so on.Please check on wikipidia if u wanna know more..
#
from random import shuffle
# two useful variables for creating Cards.

SUITE = 'H D S C'.split()
RANKS ='2 3 4 5 6 7 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class.This object will create a deck of cards to
    initiate play.You can then use this Deck list of cards to split
    in half and give to the players.It will use SUITE and RANKS to
    create the deck.It should also have a method for splitting/ cutting
    the deck in half and shuffling the deck

    """
    pass

class Hand:
    """
    This is the Hand class.Each player has a hand, and can add or remove
    cards from the hand.There should be a an add and remove card method here.

    """
    pass

class Player:
    """
    This is the player class, which takes in a name and an instance of
    a hand class object.The player can then paly cards and check if
    they still have cards.

    """
    pass

#########################################
####### GAME PLAY ######################
########################################

print("Welcome to war, let's begin....")

