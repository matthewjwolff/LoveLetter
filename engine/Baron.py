'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card
from engine.Action import Action

class Baron(Card):
    '''
    Baron (2) Compare hands; lower hand is out.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.person = "Baron"
        self.value = 3
    
    def perform(self, action, players, engine, deck):
        # select player with perceived lower card (>2)
        # compare card values
        # if their hand has a higher value, remove self and self.hand
        # if self hand has a higher value, remove target and target.hand
        # if equal, discard baron, nothing happens
        
        # It's ok to directly discard here. The player has already lost.
        if action.target.hand.value > action.doer.hand.value:
            engine.eliminate(action.doer)
        elif action.target.hand.value < action.doer.hand.value:
            engine.eliminate(action.target)

    # TODO: verify baron heuristic
    def getHeuristic(self, bot, otherCard, players):
        for player in bot.playerRanges:
            rangeEstimate = bot.playerRanges[player]
            if len(bot.playerRanges[player]) == 0:
                return [otherCard.value, player, None]
            elif self.value > rangeEstimate[len(rangeEstimate)-1]:
                # return default
                return [otherCard.value, player, None]
        if bot.isAggressive and otherCard.value == 4:
            return [0, bot.chooseRandom(players), None]
        elif not bot.isAggressive and otherCard.value == 5:
            return [0, bot.chooseRandom(players), None]
        else:
            return [otherCard.value, bot.chooseRandom(players), None]

