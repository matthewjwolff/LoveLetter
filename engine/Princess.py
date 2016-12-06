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

    def perform(self, action, players, grave, deck):
        # remove player from the round if used
        # otherwise hold onto card at all costs
        players.remove(action.doer)