'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Countess(Card):
    '''
    Countess (1) Discard if caught with king or prince.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        person = "Countess"
        value = 7
        count = 0

    def perform(self, player, card):
    	# if king or prince in hand when drawn -> move self to gy
    	# if not -> hold onto card???
    	# additionally: ability to bluff--but how?
        