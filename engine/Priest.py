'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Priest(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        person = "Priest"
        value = 2
        count = 0

    def perform(self, player, card):
    	# reveal another player's hand
    	# add to knowledge base?
        