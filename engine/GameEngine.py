'''
Created on Nov 3, 2016

The game loop runner

@author: mjw
'''

from .Deck import Deck
from engine.Princess import Princess
from engine.Action import Action

class GameEngine(object):
    '''
    The engine registers players, instantiates the game, runs the gameplay 
    loop, and executes actions that transition the game from state to state. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.origplayers = []
        self.deck = Deck()
        self.running = False
        self.grave = []
        self.discarded = None
    
    def addPlayer(self, player):
        self.origplayers.append(player)
    
    def runGame(self):
        # make a NEW list
        self.players = list(self.origplayers)
        assert len(self.players) >= 2
        for player in self.players:
            player.assignHand(self.deck.getCard())
        # discard one
        self.discarded = self.deck.getCard()
        self.running = True
        while self.running == True :
            for player in self.players :
                player.handmaidenFlag = False
                card = self.deck.getCard()
                # I changed my mind, no deep copying

                # Note, API change. Player is notified of the card dealt, 
                # remaining cards in the deck, the graveyard, and the
                # list of players
                
                # TODO: implement handmaid functionality
                action = player.getAction(card, len(self.deck.shuffled), 
                                          self.grave, self.players)
                # update the player's hand
                if action.playedCard == player.hand:
                    # If the player chose to play the card he had kept,
                    # then replace the card in his hand with the card from
                    # the deck
                    player.hand = card
                action.playedCard.perform(action, self.players, self, self.deck)
                # Tell other players that a play occurred
                for oplayer in self.origplayers:
                    # TODO: give all players notification
                    if oplayer != player:
                        oplayer.notifyOfAction(action, self.grave)
                self.grave += [action]
                # End the game if nobody remains or the deck is empty
                if len(self.players) == 1 or self.deck.size()==0:
                    # Yes I could make this into a proper while loop
                    self.running = False
        winner = self.players[0]
        # TODO: handle ties?
        for player in self.players:
            if player.hand.value > winner.hand.value:
                winner = player
        return winner
    
    def discard(self, player, card):
        '''
        Safely force a player to discard a card, and apply any effects if necessary.
        ex: the prince forces a princess discard, that player should lose
        '''
        if type(card)==Princess:
            self.players.remove(player)
        self.grave.append(Action(player, card, None, None))
