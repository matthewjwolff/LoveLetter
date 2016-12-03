'''
Created on Dec 2, 2016

@author: mjw
'''

class Action(object):
    '''
    Simple struct to contain the necessary information to return to the engine
    '''

    def __init__(self, doer, playedCard, target, guess):
        '''
        playedCard is the card that the player wishes to play
        
        target is the player that the player wishes to perform the action upon.
        This target can be the player (in the case of the Handmaid)
        
        guess is the card type (class) that the player guesses (in the case of the Guard)
        do not construct a class. not that it would do anything? 
        '''
        self.doer = doer
        self.playedCard = playedCard
        self.target = target
        self.guess = guess
        
        