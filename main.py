'''
Created on Nov 3, 2016

@author: mjw
'''

from player.RandomAI import RandomAI
from engine.GameEngine import GameEngine
from debug.DebugEngine import DebugEngine

def main():
    game = DebugEngine()
    p1 = RandomAI()
    p2 = RandomAI()
    game.addPlayer(p1)
    game.addPlayer(p2)
    winner = game.runGame()
    print ("The winner of the game is "+str(winner))

if __name__ == '__main__':
    main()
