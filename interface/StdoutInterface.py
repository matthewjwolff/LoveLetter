'''
Created on Dec 2, 2016

@author: mjw
'''
from player.HumanProxy import HumanProxy
from engine.Card import Card
from engine.Action import Action

class StdoutInterface(object):
    '''
   A rather poor implementation of CLI user input using print statements
    '''
    
    def notifyCallback(self, action):
        print("Player "+action.doer+" has played "+action.playedCard+" on "+action.target)
        
    def actionCallback(self, dealtcard, deckSize, gravestate, players):
        print("You have been dealt a "+dealtcard.class_name)
        chosen = False
        cardChoice = 0
        playerChoice = 0
        guessChoice = 0
        while(not chosen):
            print("What will you play?")
            print("1. "+self.proxy.hand)
            print("2. "+dealtcard)
            cardChoice = input(">")
            if cardChoice > 2 or cardChoice < 1:
                print("Bad choice")
            else:
                chosen = True
        
        chosen = False
        while(not chosen):
            print("On whom  will you play that? ")
            for i in range(len(players)):
                print(i+". "+players[i])
            playerChoice = input(">")
            if playerChoice < 0 or playerChoice > len(players):
                print("Bad choice")
            else:
                chosen = True
        chosen = False
        while(not chosen):
            print("What card do you guess?")
            for i in range(len(Card.cardTypes)):
                print(i+". "+Card.cardTypes[i])
            guessChoice = input(">")
            if guessChoice < 0 or guessChoice > len(Card.cardTypes):
                print("Bad choice")
            else:
                chosen = True
        return Action(self.proxy, self.proxy.hand if cardChoice == 0 else dealtcard, players[playerChoice], Card.cardTypes[guessChoice])
                
    def __init__(self):
        self.proxy = HumanProxy(self.notifyCallback, self.actionCallback)
        