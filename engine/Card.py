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
    
    The card will also serve as the holder of the "action" state. More 
    specifically, if the card's effect needs to target a player, this class 
    will hold a reference to that player. If the card's effect creates 
    publicly-available information, that information will also be stored on 
    this class. By doing this, browsing the graveyard will also browse known
    information
    '''
    person = '' # type of card
    value = 0 # card value/ranking 
    count = 0 # number of cards of this type in game??? need???

    '''
    note to matt: how do you want to keep track of count
    of cards in game?
    '''
    
    # Note to kristen: if you need more parameters, add them in and I'll 
    # refactor the engine to work with it

    def perform(self, action, players, grave, deck):
        self.type = person # return parameters on check
        self.value = value
        self.count = count
