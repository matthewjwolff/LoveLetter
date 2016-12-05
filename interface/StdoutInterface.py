'''
Created on Dec 2, 2016

@author: mjw
'''
from player.HumanProxy import HumanProxy
from engine.util import cardTypes
from engine.Action import Action

class StdoutInterface(object):
    '''
   A rather poor implementation of CLI user input using print statements
    '''
    
    def notifyCallback(self, action):
        print("Player "+action.doer+" has played "+action.playedCard+" on "+action.target)
        
    def actionCallback(self, dealtcard, deckSize, gravestate, players):
        print("You have been dealt a "+dealtcard.__class__.__name__)
        chosen = False
        cardChoice = 0
        playerChoice = 0
        guessChoice = 0
        while(not chosen):
            print("What will you play?")
            print("1. "+self.proxy.hand.__class__.__name__)
            print("2. "+dealtcard.__class__.__name__)
            cardChoice = int(input(">"))
            if cardChoice > 2 or cardChoice < 1:
                print("Bad choice")
            else:
                chosen = True
        
        chosen = False
        while(not chosen):
            print("On whom  will you play that? ")
            for i in range(len(players)):
                print(str(i)+". "+str(players[i]))
            playerChoice = int(input(">"))
            if playerChoice < 0 or playerChoice > len(players):
                print("Bad choice")
            else:
                chosen = True
        if playerChoice==0:
            chosen = False
            while(not chosen):
                print("What card do you guess?")
                for i in range(len(cardTypes)):
                    print(str(i)+". "+cardTypes[i].__name__)
                guessChoice = int(input(">"))
                if guessChoice < 0 or guessChoice > len(cardTypes):
                    print("Bad choice")
                else:
                    chosen = True
        return Action(self.proxy, self.proxy.hand if cardChoice == 0 else dealtcard, players[playerChoice], cardTypes[guessChoice])
                
    def __init__(self, name):
        self.proxy = HumanProxy(self.actionCallback, self.notifyCallback, name)
        