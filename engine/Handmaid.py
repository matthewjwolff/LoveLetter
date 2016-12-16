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
        self.person = "Handmaid"
        self.value = 4

    def perform(self, action, players, engine, deck):
        # TODO: refactor engine to work handmaid
        action.doer.handmaidenFlag = True

    # Value of playing this card is the value of the card kept in hand.
    # Same as king, priest, prince
    # TODO: better handmaid heuristic
    def getHeuristic(self, bot, otherCard, players):
        return [otherCard.value, bot, None]