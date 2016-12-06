'''
Created on Dec 5, 2016

@author: mjw
'''
from engine.GameEngine import GameEngine
from debug.DebugDeck import DebugDeck
from debug.NonRandomDeck import NonRandomDeck

class DebugEngine(GameEngine):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.origplayers = []
        self.deck = NonRandomDeck()
        self.running = False
        self.grave = []
        self.discarded = None