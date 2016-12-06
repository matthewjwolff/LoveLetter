'''
Created on Dec 5, 2016

Hard AI player

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

from . import Player
from random import choice
from engine.Action import Action


class HardAI(Player):
    '''
    An AI that monitors other players' actions and the state of the graveyard
    to make its action decisions. The AI has two different playstyles: Aggressive
    and Defensive, that help it make more informed decisions.
    '''

    def __init__(self, playstyle):
        # index == value of card (1-indexed)
        self.cardsInPlay = [0, 5, 2, 2, 2, 2, 1, 1, 1]
        self.playerRanges = {}

    def getAction(self, dealtCard, deckSize, graveState, players):
        player = self
        guess = None

        if self.hand.value() > dealtCard.value():
            chosenCard = dealtCard
        else:
            chosenCard = self.hand

        # Cards that require player to target someone
        targetCards = [1, 2, 3, 4, 6]

        if chosenCard.value() in targetCards:
            player = self.chooseRandom(players)

            if isinstance(chosenCard, Guard):
                guess = self.chooseRandomCard()

        return Action(self, chosenCard, player, guess)

    def notifyOfAction(self, action, graveState):
        # Decrement amount of cards in play
        # TODO: Account for cards in hand
        # TODO: If action.doer is you, then don't decrement
        self.cardsInPlay[action.playedCard] -= 1

        # initialize players on first turn
        if action.doer not in self.playerRanges.keys():
            self.playerRanges[action.doer] = [1,2,3,4,5,6,7,8]

        # if discarded card is in player range - reset range
        if action.playedCard.value() in self.playerRanges[action.doer]:
            self.playerRanges[action.doer] = [1, 2, 3, 4, 5, 6, 7, 8]

        # if Countess discarded, high probability of Prince, King, Princess
        if isinstance(action.playedCard, Countess):
            self.playerRanges[action.doer] = [5,6,8]

        elif isinstance(action.playedCard, Baron):
            # Action of discarding after comparing cards
            loserAction = graveState[graveState.length()-2]
            lower = loserAction.playedCard.value()
            if action.doer == loserAction.doer:
                self.playerRanges[action.target] = range(lower+1, 9)
            else:
                self.playerRanges[action.doer] = range(lower + 1, 9)

        elif isinstance(action.playedCard, Priest):
            self.playerRanges[action.target] = self.priestKnowledge


        elif isinstance(action.playedCard, Guard):
            self.playerRanges[action.target].remove(action.guess)



    def chooseRandom(self, players):
        player = self
        while player == self:
            player = choice(players)
        return player

    def chooseRandomCard(self):
        chosen = 0
        while (chosen == 0):
            chosen = choice(self.cardsInPlay)
        return self.getCardObject(chosen)

    def getCardObject(self, index):
        cardObjects = [None, Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess]
        return cardObjects[index]

    def getPriestKnowledge(self, player, card):
        self.priestKnowledge= card
