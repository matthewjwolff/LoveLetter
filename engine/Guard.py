'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card
from engine.Action import Action
from random import choice

class Guard(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.person = "Guard"
        self.value = 1

    def perform(self, action, players, engine, deck):
        # guess a target's card
        # if correct, remove the target from game
        # if wrong, discard guard
        if action.guess == type(action.target.hand):
            engine.eliminate(action.target)

    # TODO: verify guard heuristic
    def getHeuristic(self, bot, otherCard, players):
        target = bot.getMinRangePlayer()
        # TODO: if guess == Guard, retry
        if len(bot.playerRanges[target])==0:
            guess = 3
        else:
            guess = choice(bot.playerRanges[target])
        return [otherCard.value, target, guess]
