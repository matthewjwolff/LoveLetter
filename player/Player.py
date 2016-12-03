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

    def getAction(self, dealtcard, deckSize, gravestate, players):
        '''
        Callback from engine to get a player's choice
        '''
        raise NotImplementedError
    
    # TODO: tell the player some initial state information when calling this
    # i.e. how many players are playing
    def assignHand(self, card):
        '''
        The engine has given the player his starting hand
        '''
        self.hand = card
        
    def notifyOfMove(self, card):
        '''
        On another player's move, this method is called for all other players 
        to serve as notification that a move occurred.
        '''
        raise NotImplementedError
    
    def __eq__(self, other):
        '''
        A way to identify the player. Useful for deepcopying
        '''
        raise NotImplementedError