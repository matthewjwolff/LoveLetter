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
    # person = Name of card (though in most cases the class name is used)
    # value = Card value/ranking

    # Get the estimated value of playing this card.
    # Note that the return of this function is a list of:
    # [ value, target player, guess for guard ]
    def getHeuristic(self, bot, otherCard, players):
        raise NotImplementedError

    def perform(self, action, players, engine, deck):
        raise NotImplementedError
