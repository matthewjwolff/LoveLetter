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
        self.person = "Countess"
        self.value = 7

    def perform(self, action, players, grave, deck):
        # if king or prince in hand when drawn -> move self to gy
        # if not -> hold onto card???
        pass
        