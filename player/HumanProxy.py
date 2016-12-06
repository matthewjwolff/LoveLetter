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


    def __init__(self, actionCallback, notifyCallback, priestCallback, name):
        self.actionCallback = actionCallback
        self.notifyCallback = notifyCallback
        self.priestCallback = priestCallback
        self.name = name
        
    def getAction(self, dealtcard, deckSize, gravestate, players):
        return self.actionCallback(dealtcard, deckSize, gravestate, players)
        
    def notifyOfAction(self, action):
        self.notifyCallback(action)
    
    def priestKnowledge(self, player, card):
        self.priestCallback(player, card)
        
    def __str__(self):
        return self.name