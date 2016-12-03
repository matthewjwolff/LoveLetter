'''
Created on Nov 13, 2016

Easy AI player 

@author: mjw
'''

from . import Player

class EasyAI(Player):
    '''
    An AI that acts as a simple-reflex agent. It can only react based on the 
    two cards it has and what has been played in the graveyard. It does not 
    have or keep knowledge of the other players, and does not extrapolate upon 
    knowledge contained in the graveyard.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def getAction(self, dealtcard, deckSize, gravestate, players):
        '''
        Callback from engine to get a player's choice
        '''
        raise NotImplementedError
    
    def notifyOfMove(self, args):
        raise NotImplementedError        