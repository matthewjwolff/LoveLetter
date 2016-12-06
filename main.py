'''
Created on Nov 3, 2016

@author: mjw
'''

from player.RandomAI import RandomAI
from engine.GameEngine import GameEngine
from debug.DebugEngine import DebugEngine
from interface.StdoutInterface import StdoutInterface
from player.EasyAI import EasyAI
from player.HardAI import HardAI

def main():

    # random, easy, aggressive, defensive
    wins = [0, 0, 0, 0]

    for i in range(2):
        game = GameEngine()
        #p1 = RandomAI()
        #p2 = RandomAI()
        p1 = StdoutInterface("Patrick Mancuso")
        p2 = HardAI(None, True)
        #p3 = HardAI(None, True)
        #p4 = HardAI(None, False)
        game.addPlayer(p1.proxy)
        game.addPlayer(p2)
        #game.addPlayer(p3)
        #game.addPlayer(p4)
        winner = game.runGame()
        print ("The winner of the game "+ str(i) +"is "+str(winner))
        if winner == p1:
            wins[0] += 1
        #elif winner == p2:
        #    wins[1] += 1
        #elif winner == p3:
        #    wins[2] += 1
        #else:
        #    wins[3] += 1

    print("Random1 Wins: " + str(wins[0]))
    #print("Random2 Wins: " + str(wins[1]))
    print("Aggressive Wins: " + str(wins[2]))
    print("Defensive Wins: " + str(wins[3]))


if __name__ == '__main__':
    main()
