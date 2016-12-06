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
        # choose player to discard hand
        # discard player's hand
        # force a redraw
        # discard card
        engine.discard(action.target, action.target.hand)


    def getHeuristic(self, bot, otherCard, players):
        return [otherCard.value, bot.chooseRandom(players), None]