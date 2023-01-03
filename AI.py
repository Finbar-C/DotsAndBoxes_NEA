from game import *
import random
# add return moves to board class

class Chain():

    def __init__(self, references: list, start: tuple):
        self.__origin = start
        self.__references = references
        self.__length = len(self.__references)
        if self.__length >= 3:
            self.__isLong = True
        else:
            self.__isLong = False
    
    def getLength(self):
        return self.__length

    def getOrigin(self):
        return self.__origin
    
    def addRef(self, ref: tuple):
        self.__references.append(ref)
        
    def generate(self, game: Game):
        pass

    def isLong(self):
        return self.__isLong

nextmoves = []

def MoveDif(Game: Game):
    if len(nextmoves) > 0:
        move = nextmoves.pop(0)
        return move
    opts = Game.ReturnAvailable()
    newOpts = []
    for i in range(len(opts)):
        newOpts.append((opts[i][0], opts[i][1]))
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
    numMovesTotal = Game.getHeight() * Game.getWidth() * 2 + Game.getHeight() + Game.getWidth()
    movesMade = numMovesTotal - len(opts)
    if numMovesTotal / movesMade > 2:
        if len(o[3]) > 0:
            choice = random.randint(0, len(o[3]) - 1)
            move = o[3][choice]
            return move
        elif len(o[1]) > 0 and len(o[0]) > 0:
            superchoice = random.randint(0, 1)
            choice = random.randint(0, len(o[superchoice]) - 1)
            move = o[superchoice][choice]
            return move
        elif len(o[1]) > 0:
            choice = random.randint(0, len(o[1]) - 1)
            move = o[1][choice]
            return move
        elif len(o[0]) > 0:
            choice = random.randint(0, len(o[0]) - 1)
            move = o[0][choice]
            return move
        else:
            choice = random.randint(0, len(o[2]) - 1)
            move = o[2][choice]
            return move
    else:
        movesRemaining = numMovesTotal - movesMade
        # goes second, winner makes last move if played properly, wants an even number of turns for player
        # try to force player to open up first chain
        chains = createChains(Game, newOpts)
    
def createChains(Game: Game, opts: list):
    visited = []
    chains = []
    for i in range(len(opts)):
        if opts[i] not in visited:
            newvis = []
            direc = direcCheck(Game, opts[i])
            generate(Game, opts[i], direc[0], newvis)
            generate(Game, opts[i], direc[1], newvis)
            for i in range(len(newvis)):
                visited.append(newvis[i])
            chain = Chain(newvis, opts[i])
            chains.append(chain)
    return chains
            

def generate(Game: Game, start: tuple, direction: str, visited: list):
    if start not in visited:
        visited.append(start)
    if direction == "E" and start[1] + 1 <= Game.getWidth():
        newPos = (start[0], start[1]+ 1)
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        generate(Game, newPos, direc[1], visited)
    elif direction == "W" and start[1] - 1 >= 0:
        newPos = (start[0], start[1] - 1)
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        generate(Game, newPos, direc[1], visited)
    elif direction == "N" and start[0] - 1 >= 0:
        newPos = (start[0] - 1, start[1])
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        generate(Game, newPos, direc[1], visited)
    elif direction == "S" and start[0] + 1 <= Game.getHeight():
        newPos = (start[0] + 1, start[1])
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        generate(Game, newPos, direc[1], visited)
    elif direction == "T":
        return
    else:
        return

def direcCheck(Game : Game, tile: tuple):
    pos = (tile[0], tile[1])
    if Game.checkClear(pos, "N") and Game.checkClear(pos, "S"):
        direc = ("E", "W")
    elif Game.checkClear(pos, "N") and Game.checkClear(pos, "E"):
        direc = ("S, W")
    elif Game.checkClear(pos, "N") and Game.checkClear(pos, "W"):
        direc = ("S", "E")
    elif Game.checkClear(pos, "S") and Game.checkClear(pos, "E"):
        direc = ("N", "W")
    elif Game.checkClear(pos, "S") and Game.checkClear(pos, "W"):
        direc = ("N", "E")
    elif Game.checkClear(pos, "E") and Game.checkClear(pos, "W"):
        direc = ("N", "S")
    else:
        direc = "T"
    return direc


    

def MoveMed(Game: Game):
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
    elif len(o[1]) > 0 and len(o[0]) > 0:
        superchoice = random.randint(0, 1)
        choice = random.randint(0, len(o[superchoice]) - 1)
        move = o[superchoice][choice]
        return move
    elif len(o[1]) > 0:
        choice = random.randint(0, len(o[1]) - 1)
        move = o[1][choice]
        return move
    elif len(o[0]) > 0:
        choice = random.randint(0, len(o[0]) - 1)
        move = o[0][choice]
        return move
    else:
        choice = random.randint(0, len(o[2]) - 1)
        move = o[2][choice]
        return move

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