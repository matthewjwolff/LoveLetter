'''
Created on Nov 26, 2016

@author: mjw
'''

from engine.Card import Card

class Handmaid(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.person = "Handmaiden"
        self.value = 4

    def perform(self, action, players, engine, deck):
        # remove player from the round selection?
        # how to do this on my end?
        # discard card
        action.doer.handmaidenFlag = True

    def getHeuristic(self, bot, otherCard):
        return [otherCard.value, self, None]