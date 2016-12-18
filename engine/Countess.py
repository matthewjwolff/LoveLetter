'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Countess(Card):
    '''
    Countess (7) Discard if caught with king or prince.
    '''
    
    person = "Countess"
    value = 7

    def perform(self, action, players, engine, deck):
        # Does not actually do anything.
        pass
