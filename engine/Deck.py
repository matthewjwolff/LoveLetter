'''
Created on Nov 3, 2016

The set of cards in the deck

@author: mjw
'''

class Deck(object):
    '''
    The Deck contains all the cards in the game. Notably, it instantiates 
    itself with a random permutation of the standard Love Letter deck and 
    exposes a way to draw from this random permutation.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def getCard(self):
        '''
        Deal a card
        '''
        pass
    
    def getState(self):
        '''
        Get a structure holding the number of remaining cards and their 
        possible types.
        Make sure to return a copy, do not give back references to the source 
        of truth
        Or do, and let the engine handle copying?
        '''
        pass