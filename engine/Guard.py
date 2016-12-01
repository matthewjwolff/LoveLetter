'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Guard(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        person = "Guard"
    	value = 1
    	count = 0

    def perform(self, player, card):
    	# pick player to "guess" type of card (can't be guard)
    	# if guess correctly -> player is out, discard card
    	# if guess wrong -> discard card
        