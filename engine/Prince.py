'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card
from engine.Action import Action

class Prince(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.person = "Prince"
        self.value = 5

    def perform(self, action, players, engine, deck):
        # discard player's hand
        engine.abnormalDiscard(action.target, action.target.hand)

    # Value of playing this card is the value of the card kept in hand.
    # Same as king, priest, handmaid
    # TODO: better prince heuristic
    def getHeuristic(self, bot, otherCard, players):
        return [otherCard.value, bot.chooseRandom(players), None]