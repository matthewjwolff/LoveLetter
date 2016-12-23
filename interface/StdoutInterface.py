'''
Created on Dec 2, 2016

@author: mjw
'''
from player.HumanProxy import HumanProxy
from engine.util import cardTypes
from engine.Action import Action
from engine.Guard import Guard

class StdoutInterface(object):
    '''
   A rather poor implementation of CLI user input using print statements
    '''
    
    def priestCallback(self, player, card):
        print("Player "+str(player)+" has a "+card.__class__.__name__)
    
    def notifyCallback(self, action, graveState):
        print("Player "+str(action.doer)+" has played "+action.playedCard.__class__.__name__+" on "+str(action.target))
        if action.playedCard==Guard:
            print("They guessed "+action.guess.__class__.__name__)
        
    def actionCallback(self, dealtcard, deckSize, gravestate, players):
        print("You have been dealt a "+dealtcard.__class__.__name__)
        chosen = False
        cardChoice = 0
        chosenCard = None
        playerChoice = 0
        guessChoice = 0
        while(not chosen):
            print("What will you play?")
            print("1. "+self.proxy.hand.__class__.__name__)
            print("2. "+dealtcard.__class__.__name__)
            cardChoice = int(input("> "))
            if cardChoice > 2 or cardChoice < 1:
                print("Bad choice")
            else:
                chosen = True
                chosenCard = self.proxy.hand if cardChoice == 1 else dealtcard
        
        chosen = False
        while(not chosen):
            print("On whom  will you play that? ")
            for i in range(len(players)):
                print(str(i)+". "+str(players[i]))
            playerChoice = int(input("> "))
            if playerChoice < 0 or playerChoice > len(players):
                print("Bad choice")
            else:
                chosen = True
        if type(chosenCard) == Guard:
            # they chose a guard, better see what they want to guess
            chosen = False
            while(not chosen):
                print("What card do you guess?")
                for i in range(len(cardTypes)):
                    print(str(i)+". "+cardTypes[i].__name__)
                guessChoice = int(input("> "))
                if guessChoice < 0 or guessChoice > len(cardTypes):
                    print("Bad choice")
                else:
                    chosen = True
        return Action(self.proxy, chosenCard, players[playerChoice], cardTypes[guessChoice])
    
    def eliminateCallback(self, player):
        print("Player "+str(player)+ " has been eliminated")
        
    def assignHandCallback(self, card, players):
        print("The game has begun. "+str(players)+" are playing.")
        print("Your initial card is "+card.__class__.__name__)
                
    def __init__(self, name=None):
        if name==None:
            print("What is your name?")
            name = input("> ")
        self.proxy = HumanProxy(self.actionCallback, self.notifyCallback, self.priestCallback, self.eliminateCallback, self.assignHandCallback, name)
        