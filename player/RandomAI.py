'''
Created on Nov 27, 2016

@author: mjw
'''
from player.Player import Player
from engine.Action import Action
import random
from engine.Baron import Baron

class RandomAI(Player):
    '''
    An AI for engine testing that makes a random choice for all actions.
    
    Alternately, it is an AI that always takes a random choice.
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def getAction(self, dealtcard, deckSize, gravestate, players):
        # TODO: Make target not self in case of non-handmaid, self in case of handmaid
        return Action(random.choice((self.hand, dealtcard)), random.choice(players), Baron)