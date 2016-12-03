'''
Created on Nov 3, 2016

The game loop runner

@author: mjw
'''

from .Deck import Deck

class GameEngine(object):
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

    def __init__(self):
        '''
        Constructor
        '''
        self.players = []
        self.deck = Deck()
        self.running = False
        self.grave = []
        self.discarded = None
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def runGame(self):
        # TODO: maintain set of original players?
        assert len(self.players) >= 2
        for player in self.players:
            player.assignHand(self.deck.getCard())
        # discard one
        self.discarded = self.deck.getCard()
        self.running = True
        while self.running == True :
            for player in self.players :
                card = self.deck.getCard()
                # I changed my mind, no deep copying

                # Note, API change. Player is notified of the card dealt, 
                # remaining cards in the deck, the graveyard, and the
                # list of players
                action = player.getAction(card, len(self.deck.shuffled), 
                                          self.grave, self.players)
                action.playedCard.perform(action, self.players, self.grave, self.deck)
                # Tell other players that a play occurred
                for oplayer in self.players:
                    if oplayer != player:
                        oplayer.notifyOfMove(action) 
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
        
