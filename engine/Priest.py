'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Priest(Card):
    '''
    classdocs
    '''
    
    person = "Priest"
    value = 2

    def perform(self, action, players, engine, deck):
        # reveal another player's hand
        action.doer.priestKnowledge(action.target, action.target.hand)
