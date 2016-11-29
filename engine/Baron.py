'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Baron(Card):
    '''
    Baron (2) Compare hands; lower hand is out.
    '''
    def __init__(self):
        '''
        Constructor
        '''
	    type = "Baron"
	    value = 2
	    count = 0
    
    def perform(self):
    	# select player with perceived lower card (>2)
    	# compare card values
    	# if player.value > 2 -> move self.card to gy; bot out
    	# if player.value < 2 -> move player.card to gy; player out
        