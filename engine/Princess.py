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
        self.person = "Princess"
        self.value = 8

    def perform(self, action, players, engine, deck):
        # Directly remove player from game. Cannot use engine.eliminate
        # because that method discards this card. 
        players.remove(action.doer)
        engine.eliminatedThisRound = action.doer