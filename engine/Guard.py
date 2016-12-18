'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Guard(Card):
    '''
    classdocs
    '''
    
    person = "Guard"
    value = 1

    def perform(self, action, players, engine, deck):
        # guess a target's card
        # if correct, remove the target from game
        # if wrong, discard guard
        if action.guess == type(action.target.hand):
            engine.eliminate(action.target)
