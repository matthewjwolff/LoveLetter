'''
Created on Nov 26, 2016

@author: mjw
'''

from engine.Card import Card

class Handmaid(Card):
    '''
    classdocs
    '''
    
    person = "Handmaid"
    value = 4

    def perform(self, action, players, engine, deck):
        # TODO: refactor engine to work handmaid
        action.doer.handmaidenFlag = True
