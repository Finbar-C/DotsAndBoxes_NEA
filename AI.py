from game import *
# add return moves to board class
def MoveDif(Game):
    pass

def MoveMed(Game):
    pass

def MoveEasy(Game):
    pass

def MoveRan(Game):
    pass

def Move(Difficulty, Game):
    if Difficulty == 0:
        return MoveRan(Game)
    elif Difficulty == 1:
        return MoveEasy(Game)
    elif Difficulty == 2:
        return MoveMed(Game)
    elif Difficulty == 3:
        return MoveDif(Game)