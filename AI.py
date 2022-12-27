from game import *
import random
# add return moves to board class
def MoveDif(Game):
    pass

def MoveMed(Game):
    pass

def MoveEasy(Game):
    pass

def MoveRan(Game):
    opts = Game.ReturnAvailable()
    length = len(opts)
    choice = random.randint(0, length-1)
    move = opts[choice]
    return move

def Move(Difficulty: int, Game: Game):
    if Difficulty == 0:
        return MoveRan(Game)
    elif Difficulty == 1:
        return MoveEasy(Game)
    elif Difficulty == 2:
        return MoveMed(Game)
    elif Difficulty == 3:
        return MoveDif(Game)