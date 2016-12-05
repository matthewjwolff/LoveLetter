'''
Created on Nov 26, 2016

@author: mjw
'''
from engine.Card import Card

class Guard(Card):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        person = "Guard"
    	value = 1

    def perform(self, action, players, grave, deck):
        # guess a target's card
        # if correct, remove the target from game
        # if wrong, discard guard
        if action.guess == type(action.target.hand):
            players.remove(action.target)
            grave.append(action.target.hand) # moves card into grave

        