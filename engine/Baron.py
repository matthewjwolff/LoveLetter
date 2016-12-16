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
        # if their hand has a higher value, eliminate doer
        # if self hand has a higher value, eliminate target
        # if equal, nothing happens
        
        if action.target.hand.value > action.doer.hand.value:
            engine.eliminate(action.doer)
        elif action.target.hand.value < action.doer.hand.value:
            engine.eliminate(action.target)

    # TODO: definitely a bad heuristic
    def getHeuristic(self, bot, otherCard, players):
        for player in bot.playerRanges:
            rangeEstimate = bot.playerRanges[player]
            # If the bot has eliminated all possibilites from the other player
            if len(rangeEstimate) == 0:
                return [otherCard.value, player, None]
            # If the highest card the player might have is less than a Baron
            elif self.value > rangeEstimate[len(rangeEstimate)-1]:
                # return default
                return [otherCard.value, player, None]
        if bot.isAggressive and otherCard.value == 4:
            # if the other card is a handmaid, we should really play the baron
            return [0, bot.chooseRandom(players), None]
        elif not bot.isAggressive and otherCard.value == 5:
            # if the other card is a prince, we should really play the baron
            return [0, bot.chooseRandom(players), None]
        else:
            return [otherCard.value, bot.chooseRandom(players), None]

