'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Baron(Card):
    '''
    Baron (2) Compare hands; lower hand is out.
    '''
    
    person = "Baron"
    value = 3
    
    def perform(self, action, players, engine, deck):
        # select player with perceived lower card (>2)
        # compare card values
        # if their hand has a higher value, eliminate doer
        # if self hand has a higher value, eliminate target
        # if equal, nothing happens
        
        if action.target.hand.value > action.doer.hand.value:
            engine.eliminate(action.doer)
        elif action.target.hand.value < action.doer.hand.value:
            engine.eliminate(action.target)
