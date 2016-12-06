'''
Created on Nov 13, 2016

Easy AI player 

@author: mjw
'''
from engine.Countess import Countess
from engine.Baron import Baron
from engine.Guard import Guard
from engine.Handmaid import Handmaid
from engine.King import King
from engine.Priest import Priest
from engine.Prince import Prince
from engine.Princess import Princess

from . import Player
from random import choice
from engine.Action import Action

class EasyAI(Player):
    '''
    An AI that acts as a simple-reflex agent. It can only react based on the 
    two cards it has and what has been played in the graveyard. It does not 
    have or keep knowledge of the other players, and does not extrapolate upon 
    knowledge contained in the graveyard.
    '''


    def __init__(self, params):
        #index == value of card (1-indexed)
        self.cardsInPlay = [0,5,2,2,2,2,1,1,1]
        
    def getAction(self, dealtCard, deckSize, graveState, players):
        player = self
        guess = None

        if self.hand.value() > dealtCard.value():
            chosenCard = dealtCard
        else:
            chosenCard = self.hand

        # Cards that require player to target someone
        targetCards = [1,2,3,4,6]

        if chosenCard.value() in targetCards:
            player = self.chooseRandom(players)

            if isinstance(chosenCard, Guard):
                guess = self.chooseRandomCard()

        return Action(self, chosenCard, player, guess)

    
    def notifyOfAction(self, action):
        self.cardsInPlay[action.playedCard] -= 1

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