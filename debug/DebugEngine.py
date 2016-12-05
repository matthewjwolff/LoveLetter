'''
Created on Dec 5, 2016

@author: mjw
'''
from engine.GameEngine import GameEngine
from debug.DebugDeck import DebugDeck

class DebugEngine(GameEngine):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.players = []
        self.deck = DebugDeck()
        self.running = False
        self.grave = []
        self.discarded = None