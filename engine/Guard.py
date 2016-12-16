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

    # Find the player the bot knows the most about, then pick one from what we 
    # know about him
    # The default choice is a Baron. 
    def getHeuristic(self, bot, otherCard, players):
        target = bot.getMinRangePlayer()
        # if we know nothing about the player, pick a default
        if len(bot.playerRanges[target])==0:
            guess = 3
        # if the only thing the player could have is a guard, pick a default
        elif len(bot.playerRanges[target])==1 and bot.playerRanges[target][0] == 1:
            guess = 3
        else:
            guess = 1
            while guess == 1:
                guess = choice(bot.playerRanges[target])
        return [otherCard.value, target, guess]
