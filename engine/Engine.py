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
    The engine registers players, instantiates the game, runs the gameplay 
    loop, and executes actions that transition the game from state to state. 
    
    It should be noted that whenever interaction from players is queried, 
    COPIES of data are delivered to the player classes, and not the actual 
    data. Remember that Python does not have protection facilities in it, so 
    there is no way to ensure that a player does not modify game data. So we 
    pass copies of data, not references to it.
    
    Also note that if data intended to be kept is returned from the player, 
    that data too will have to be copied. There is no guarantee that the 
    player has released control of that data. 
    
    Yes we're the only ones programming this, and yes we could just have the 
    players not touch global state, but we'll use this as an opportunity to 
    exercise good coding practice.
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self.players = []
        self.deck = Deck()
        self.running = False
        self.grave = Grave()
        self.discarded = None
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def runGame(self):
        assert len(self.players >= 2)
        for player in self.players:
            player.assignHand(self.deck.getCard())
        # discard one
        self.discarded = self.deck.getCard()
        while self.running == True :
            for player in self.players :
                card = self.deck.getCard()
                # Don't let players modify real stuff
                deckState = deepcopy(self.deck.getState())
                graveState = deepcopy(self.grave.getState())
                playercopy = deepcopy(self.players)
                action = player.getAction(card, deckState, 
                                          graveState, playercopy)
                self.grave.discard(action.card, player)
                # End the game if nobody remains or the deck is empty
                action.card.perform(action)
                if len(self.players) == 1 or self.deck.size()==0:
                    # Yes I could make this into a proper while loop
                    self.running = False
        winner = self.players[0]
        # TODO: handle ties?
        for player in self.players:
            if player.hand.value > winner.hand.value:
                winner = player
        return winner
        