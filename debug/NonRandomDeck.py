'''
Created on Dec 6, 2016

@author: mjw
'''

from engine.Deck import Deck
from engine.Baron import Baron
from engine.Countess import Countess
from engine.Prince import Prince
from engine.Priest import Priest
from engine.Princess import Princess
from engine.King import King
from engine.Guard import Guard
from engine.Handmaid import Handmaid

class NonRandomDeck(Deck):
    '''
   A Deck that always returns the same order of cards
    '''


    def __init__(self):
        self.shuffled = [Guard(), Prince(), Guard(), Countess(), Baron(), Guard(), King(), Guard(), Baron(), Handmaid(), Princess(), Priest(), Priest(), Guard(), Prince(), Handmaid()]
#         self.shuffled = [Princess(), Countess(), King(), Guard(), Guard(), 
#             Handmaid(), Handmaid(), Baron(), Baron(), Priest(), 
#             Priest(), Guard(), Guard(), Guard(), Prince(), Prince()]
        