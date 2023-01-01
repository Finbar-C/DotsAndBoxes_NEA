from game import *
import random
# add return moves to board class
def MoveDif(Game: Game):
    pass

def MoveMed(Game: Game):
    pass

def MoveEasy(Game: Game):
    opts = Game.ReturnAvailable()
    length = len(opts)
    o = [[] for _ in range(4)]
    for i in range(length):
        test = opts[i]
        matchedTest = Game.MatchedPlace((test[0], test[1]), test[2])
        level_t1 = optLevel(test, Game)
        if matchedTest != None:
            level_t2 = optLevel(matchedTest, Game)
        else:
            level_t2 = 0
        if level_t1 >= level_t2:
            o[level_t1].append(test)
        else:
            o[level_t2].append(test)
    
    if len(o[3]) > 0:
        choice = random.randint(0, len(o[3]) - 1)
        move = o[3][choice]
        return move
    elif len(o[2]) > 0:
        choice = random.randint(0, len(o[2]) - 1)
        move = o[2][choice]
        return move
    elif len(o[1]) > 0:
        choice = random.randint(0, len(o[1]) - 1)
        move = o[1][choice]
        return move
    else:
        choice = random.randint(0, len(o[0]) - 1)
        move = o[0][choice]
        return move


def MoveRan(Game: Game):
    opts = Game.ReturnAvailable()
    length = len(opts)
    choice = random.randint(0, length-1)
    move = opts[choice]
    return move

def optLevel(opt: tuple, Game: Game):
    dirs = ["N", "S", "E", "W"]
    dirs.remove(opt[2])
    count = 0
    for i in range(3):
        if not Game.checkClear((opt[0], opt[1]), dirs[i]):
            count += 1
    return count


def Move(Difficulty: int, Game: Game):
    if Difficulty == 0:
        return MoveRan(Game)
    elif Difficulty == 1:
        return MoveEasy(Game)
    elif Difficulty == 2:
        return MoveMed(Game)
    elif Difficulty == 3:
        return MoveDif(Game)