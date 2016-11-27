'''
Created on Nov 3, 2016

The set of cards in the deck

@author: mjw
'''
from cards import Baron, Countess, Prince, Princess, King, Handmaid, Priest, Guard
from random import randint

class Deck(object):
    '''
    The Deck contains all the cards in the game. Notably, it instantiates 
    itself with a random permutation of the standard Love Letter deck and 
    exposes a way to draw from this random permutation.
    '''
    
    unshuffled = [Princess, Countess, King, Prince, Prince, 
                  Handmaid, Handmaid, Baron, Baron, Priest, 
                  Priest, Priest, Guard, Guard, Guard, Guard, Guard]

    def __init__(self, params):
        '''
        Randomly pull constructors out of the unshuffled list. Don't pull the 
        same one twice. Then create an instance and add to the deck
        '''
        self.shuffled = []
        indices = list(range(0, len(self.unshuffled)))
        while len(indices) != 0:
            index = randint(0, len(indices) - 1)
            clazz = self.unshuffled[index]
            self.shuffled += [clazz()]
            indices.remove(index)
    
    def getCard(self):
        if len(self.shuffle) == 0:
            return None
        else:
            top = self.shuffled[0]
            self.shuffled = self.shuffled[1:]
            return top