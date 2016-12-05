'''
Created on Dec 5, 2016

@author: mjw
'''
from debug.DebugCard import DebugCard
from engine.Deck import Deck

class DebugDeck(Deck):
    '''
    classdocs
    '''


    def __init__(self):
        # Gotta have enough to play (one per player, one to discard, and one to deal)
        self.shuffled = [DebugCard(), DebugCard(), DebugCard(), DebugCard()]
        