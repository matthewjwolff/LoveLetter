'''
Created on Nov 3, 2016

The game loop runner

@author: mjw
'''

from . import Deck
from . import Grave
from copy import deepcopy

class Engine(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.players = []
        self.deck = Deck()
        self.running = False
        self.grave = Grave()
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def runGame(self):
        assert len(self.players >= 2)
        # TODO: initialize game
        while self.running == True :
            for player in self.players :
                card = self.deck.getCard()
                deckState = self.deck.getState()
                graveState = self.grave.getState()
                # Don't let players modify real players
                # TODO: Make a equality check
                # TODO: check for full copying
                playercopy = deepcopy(self.players)
                action = player.getAction(card, deckState, graveState, playercopy)
                # TODO: organize
                action.do()
                self.grave.discard(card, player)
            
        