'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card
from random import choice

class Countess(Card):
    '''
    Countess (7) Discard if caught with king or prince.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.person = "Countess"
        self.value = 7

    def perform(self, action, players, engine, deck):
        # Does not actually do anything.
        pass

    def getHeuristic(self, bot, otherCard, players):
        # TODO: implement early/mid/late game
        # TODO: engine-wide change of countess / handmaid target to None
        if choice(range(10)) == 1:
            return [10, bot, None]
        else:
            return [0, bot, None]