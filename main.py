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
    game = GameEngine()
    # p1 = StdoutInterface("Jerry Lewis")
    # for hard ai
    # HardAI(playstyle (not used?), isAggressive)
    p2 = HardAI(None, True)
    p3 = HardAI(None, False)
    p4 = HardAI(None, True)
    #game.addPlayer(p1.proxy)
    game.addPlayer(p2)
    game.addPlayer(p3)
    game.addPlayer(p4)
    winner = game.runGame()
    print ("The winner of the game is "+str(winner))

if __name__ == '__main__':
    main()
