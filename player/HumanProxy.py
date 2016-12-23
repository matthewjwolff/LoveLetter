'''
Created on Dec 2, 2016

@author: mjw
'''
from player.Player import Player

class HumanProxy(Player):
    '''
    A class that acts on behalf of a human player. A class in the interface 
    folder should use an instance of this class to perform actions.
    
    This class will register callbacks and execute those callbacks to the 
    interface.
    
    Seems redundant? Sure. But I predict it will give more freedom to interface 
    developers, so that they don't have to design their interface around my API.
    '''


    def __init__(self, actionCallback, notifyCallback, priestCallback, eliminateCallback, assignHandCallback, name):
        self.actionCallback = actionCallback
        self.notifyCallback = notifyCallback
        self.priestCallback = priestCallback
        self.eliminateCallback = eliminateCallback
        self.assignHandCallback = assignHandCallback
        self.name = name
        
    def assignHand(self, card, players):
        Player.assignHand(self, card, players)
        self.assignHandCallback(card, players)
        
    def getAction(self, dealtCard, deckSize, graveState, players):
        return self.actionCallback(dealtCard, deckSize, graveState, players)
    
    def notifyOfAction(self, action, graveState):
        self.notifyCallback(action, graveState)
    
    def priestKnowledge(self, player, card):
        self.priestCallback(player, card)
        
    def notifyEliminate(self, player):
        self.eliminateCallback(player)
        
    def __str__(self):
        return self.name