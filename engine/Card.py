'''
Created on Nov 9, 2016

Base class for all cards.

@author: mjw
'''

class Card(object):
    '''
    The base class for all cards in the game. Each card has a point value 
    from 1-8, a callback to perform its effect, and (possibly) a tally of the 
    total number of this type of card in a game.
    '''

    def perform(self, action):
        raise NotImplementedError