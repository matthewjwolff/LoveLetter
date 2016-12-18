'''
Created on Dec 17, 2016

@author: mjw
'''
from interface.StdoutInterface import StdoutInterface
from engine.GameEngine import GameEngine
from player.RandomAI import RandomAI
from player.EasyAI import EasyAI
from player.HardAI import HardAI

def main():
    player = StdoutInterface().proxy
    print("Number of RandomAI")
    numRand = int(input("> "))
    print("Number of EasyAI")
    numEasy = int(input("> "))
    print("Number of HardAI")
    numHard = int(input("> "))
    engine = GameEngine()
    engine.addPlayer(player)
    for i in range(numRand):
        engine.addPlayer(RandomAI())
    for i in range(numEasy):
        engine.addPlayer(EasyAI())
    for i in range(numHard):
        engine.addPlayer(HardAI(True))
    winner = engine.runGame()
    print("The winner is "+str(winner))

if __name__ == '__main__':
    main()