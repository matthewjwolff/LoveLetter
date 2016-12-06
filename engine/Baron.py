'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card
from engine.Action import Action

class Baron(Card):
    '''
    Baron (2) Compare hands; lower hand is out.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        person = "Baron"
        value = 3
    
    def perform(self, action, players, grave, deck):
        # select player with perceived lower card (>2)
        # compare card values
        # if their hand has a higher value, remove self and self.hand
        # if self hand has a higher value, remove target and target.hand
        # if equal, discard baron, nothing happens
        if action.target.hand.value > action.doer.hand.value:
            grave.append(Action(action.doer, action.doer.hand, None, None))
            players.remove(action.doer)
        elif action.target.hand.value < action.doer.hand.value:
            grave.append(Action(action.target, action.target.hand, None, None))
            players.remove(action.target)

        