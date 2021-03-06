'''
Created on Nov 8, 2016

Base class for players

@author: mjw
'''

class Player(object):
    '''
    This is the base class for all Player classes.
    
    In a language with a more thorough class inheritance system, this class 
    would be an abstract class or an interface.
    
    In python, there's no distinction between such things, so this class 
    should be used as a model.
    
    Types of players may include local players using a GUI, computer player 
    using an AI, networked "player" proxy that receives moves from a nonlocal 
    player, and networked "player" client that sends his moves to the proxy 
    that is acting on his behalf.
    '''

    def getAction(self, dealtCard, deckSize, graveState, players):
        '''
        Callback from engine to get a player's choice
        '''
        raise NotImplementedError
    
    def assignHand(self, card, players):
        '''
        The engine has given the player his starting hand
        '''
        self.hand = card
        
    def notifyOfAction(self, action, graveState):
        '''
        On another player's move, this method is called for all other players 
        to serve as notification that a move occurred.
        '''
        raise NotImplementedError
    
    def notifyEliminate(self, player):
        '''
        A player has been eliminated from the game
        '''
        raise NotImplementedError

    def priestKnowledge(self, player, card):
        '''
        When the Priest is played, add knowledge of a target player's
        hand to self.
        '''
        raise NotImplementedError
