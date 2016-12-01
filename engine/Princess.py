'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Princess(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        person = "Princess"
        value = 8
        count = 0

    def perform(self, player, card):
    	# remove player from the round if used
    	# otherwise hold onto card at all costs
        