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

    def perform(self, action, players, grave, deck):
        # guess a target's card
        # if correct, remove the target from game
        # if wrong, discard guard
        if action.guess == type(action.target.hand):
            players.remove(action.target)
            grave.append(Action(None, action.target.hand, None, None)) # moves card into grave

    def getHeuristic(self, bot, otherCard):
        target = bot.getMinRange()
        guess = choice(bot.playerRanges[target])
        return [otherCard.value, target, guess]