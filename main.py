'''
Created on Nov 3, 2016

@author: mjw
'''

from player.RandomAI import RandomAI
from engine.GameEngine import GameEngine

def main():
    game = GameEngine()
    p1 = RandomAI()
    p2 = RandomAI()
    game.addPlayer(p1)
    game.addPlayer(p2)
    game.runGame()

if __name__ == '__main__':
    main()
