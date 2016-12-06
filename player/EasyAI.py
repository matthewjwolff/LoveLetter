'''
Created on Nov 13, 2016

Easy AI player 

@author: Ben, Patrick, Josh
'''
from engine.Countess import Countess
from engine.Baron import Baron
from engine.Guard import Guard
from engine.Handmaid import Handmaid
from engine.King import King
from engine.Priest import Priest
from engine.Prince import Prince
from engine.Princess import Princess

from .Player import Player
from random import choice
from engine.Action import Action

class EasyAI(Player):
    '''
    An AI that acts as a simple-reflex agent. It can only react based on the 
    two cards it has and what has been played in the graveyard. It does not 
    have or keep knowledge of the other players, and does not extrapolate upon 
    knowledge contained in the graveyard.
    '''
    
    numBots = 0

    def __init__(self):
        #index == value of card (1-indexed)
        self.cardsInPlay = [0,5,2,2,2,2,1,1,1]
        self.number = EasyAI.numBots
        EasyAI.numBots += 1
        
    def getAction(self, dealtCard, deckSize, graveState, players):
        player = self
        guess = None

        if self.hand.value > dealtCard.value:
            chosenCard = dealtCard
        else:
            chosenCard = self.hand

        # Cards that require player to target someone
        targetCards = [1,2,3,4,6]

        if chosenCard.value in targetCards:
            player = self.chooseRandom(players)

            if isinstance(chosenCard, Guard):
                guess = self.chooseRandomCard()
                
        if type(chosenCard) == Handmaid:
            player = self
            
        return Action(self, chosenCard, player, guess)

    def priestKnowledge(self, player, card):
        # Called when the bot plays the priest, the method gives the bot
        # knowledge of what the priest gave it
        pass
    
    def notifyOfAction(self, action, graveState):
        self.cardsInPlay[action.playedCard.value] -= 1

    def chooseRandom(self, players):
        player = self
        while player == self:
            player = choice(players)
        return player

    def chooseRandomCard(self):
        chosen = 0
        while(chosen == 0):
            chosen = choice(self.cardsInPlay)
        return self.getCardObject(chosen)

    def getCardObject(self, index):
        cardObjects = [None, Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess]
        return cardObjects[index]
    
    def __str__(self):
        return "EasyAI"+str(self.number)
