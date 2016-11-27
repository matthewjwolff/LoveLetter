'''
Created on Nov 3, 2016

The set of already-played cards, including who played them and in what order.

@author: mjw
'''

class Grave(object):
    '''
    The graveyard contains the list of played cards, who was targeted, and 
    what happened because of it.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getState(self):
        '''
        Get played cards in the order they were played and who played them
        Make sure to return a copy, do not give back references to the source 
        of truth
        
        Or do, and let the engine handle copying?
        '''
        pass
    
    def discard(self, card, player):
        '''
        Add a card to the discard pile and note who played it
        '''
        pass