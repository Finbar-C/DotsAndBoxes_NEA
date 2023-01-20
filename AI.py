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
    
    def getRefs(self):
        return self.__references

    def getOrigin(self):
        return self.__origin
    
    def addRef(self, ref: tuple):
        self.__references.append(ref)
    
    def popRef(self, ref: tuple):
        for i in range(len(self.__references)):
            if self.__references[i] == ref:
                res = self.__references.pop(i)
                return res
    
    def popNoRef(self):
        res = self.__references.pop()
        return res
        
    def generate(self, game: Game):
        pass

    def isLong(self):
        if self.__length >= 3:
            self.__isLong = True
        else:
            self.__isLong = False
        return self.__isLong

nextmoves = []

#####################################################
# Skill set B - Simple User-Defined Algorithms      #
# The MoveDif function splits given move options    #
# into groups based on how many sides they have, and#
# then depending on how far into the game it is and #
# which moves are available, it will decide which   #
# move to make                                      #
#####################################################

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
        print(chains)
        effectiveMovesRemaining = 0
        for i in range(len(chains)):
            if chains[i].isLong() and i != len(chains) - 1:
                effectiveMovesRemaining += 2
            else:
                effectiveMovesRemaining += 1
        effectiveMovesRemaining += 1
        if len(o[3]) == 1:
            inChain = False
            for i in range(len(chains)):
                refs = chains[i].getRefs()
                if (o[3][0][0], o[3][0][1]) in refs:
                    current = chains[i]
                    pos = (o[3][0][0], o[3][0][1])
                    inChain = True
            if inChain and current.getLength() == 1:
                move = o[3][0]
            elif inChain:
                move = playChain(current, pos, Game)
            else:
                move = o[3][0]
            return move
        elif len(o[3]) == 2:
            for i in range(len(chains)):
                refs = chains[i].getRefs()
                if (o[3][0][0], o[3][0][1]) in refs:
                    c1 = chains[i]
                    p1 = (o[3][0][0], o[3][0][1])
                    l1 = c1.getLength()
                if (o[3][1][0], o[3][1][1]) in refs:
                    c2 = chains[i]
                    p2 = (o[3][1][0], o[3][1][1])
                    l2 = c2.getLength()
            if l1 > 2 and l2 > 2:
                move = playChain(c1, p1, Game)
            elif l1 == 2 and l2 > 2:
                move = playChain(c2, p2, Game)
            elif l1 > 2 and l2 == 2:
                move = playChain(c1, p1, Game)
            elif l1 == 2 and l2 == 2:
                move = o[3][0]
            elif l1 == 1 and l2 == 2:
                move = o[3][0]
            elif l2 == 1 and l1 == 2:
                move = o[3][1]
        
        elif len(o[3]) > 2:
            choice = random.randint(0,(len(o[3])-1))
            move = o[3][choice]

        else:
            if len(o[1]) > 0 and len(o[0]) > 0:
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


def playChain(chain: Chain, ref: tuple, Game: Game):
    if chain.isLong():
        reference = chain.popRef(ref)
        dirs = direcCheck(Game, ref)
        if Game.checkClear(reference, dirs[0]):
            move = (reference[0], reference[1], dirs[0])
            return move
        else:
            move = (reference[0], reference[1], dirs[1])
            return move
    else:
        move = doubleBox(chain, Game, ref)
        return move

def doubleBox(chain: Chain, Game: Game, ref: tuple):
    ref1 = chain.popRef(ref)
    ref2 = chain.popNoRef()
    direc = direcCheck(ref1)
    matchref = Game.MatchedPlace(ref1, direc)
    direc2 = direcCheck(ref2)
    if direc2[0] != matchref[2]:
        move = (ref2[0], ref2[1], direc2[0])
    else:
        move = (ref2[0], ref2[1], direc2[1])
    return move

    
################################################################
# Skill set A - Dynamic Generation of Objects                  #
# createChains function generates chains based on the current  #
# state of the board, which is dependent on size and shape of  #
# the board as well as the moves that have been made           #
################################################################
    
def createChains(Game: Game, opts: list):
    visited = []
    chains = []
    for i in range(len(opts)):
        if opts[i] not in visited:
            newvis = []
            direc = direcCheck(Game, opts[i])
            generate(Game, opts[i], direc[0], newvis)
            if len(direc) == 2:
                generate(Game, opts[i], direc[1], newvis)
            for i in range(len(newvis)):
                visited.append(newvis[i])
            chain = Chain(newvis, opts[i])
            chains.append(chain)
    return chains
            
################################################################
# Skill set A - Recursive Algorithms                           #
# generate function recursively calls itself while creating a  #
# chain object for use by the Difficult opponent algorithm     #
################################################################

def generate(Game: Game, start: tuple, direction: str, visited: list):
    if start not in visited:
        visited.append(start)
    if direction == "E" and start[1] + 1 < Game.getWidth():
        newPos = (start[0], start[1]+ 1)
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        if len(direc) == 2:
            generate(Game, newPos, direc[1], visited)
    elif direction == "W" and start[1] - 1 >= 0:
        newPos = (start[0], start[1] - 1)
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        if len(direc) == 2:
            generate(Game, newPos, direc[1], visited)
    elif direction == "N" and start[0] - 1 >= 0:
        newPos = (start[0] - 1, start[1])
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        if len(direc) == 2:
            generate(Game, newPos, direc[1], visited)
    elif direction == "S" and start[0] + 1 < Game.getHeight():
        newPos = (start[0] + 1, start[1])
        if newPos in visited:
            return
        direc = direcCheck(Game, newPos)
        generate(Game, newPos, direc[0], visited)
        if len(direc) == 2:
            generate(Game, newPos, direc[1], visited)
    elif direction == "T":
        return
    else:
        return

################################################################
# Skill Set A - Pattern Recognition in user-defined algorithmn #
# Data in the board is analysed to decide whether chains       #
# continue, and their directions.                              #
################################################################

def direcCheck(Game : Game, tile: tuple):
    pos = (tile[0], tile[1])
    tcount = 0
    if Game.checkClear(pos, "N"):
        tcount+=1
    if Game.checkClear(pos, "S"):
        tcount+=1
    if Game.checkClear(pos, "E"):
        tcount+=1
    if Game.checkClear(pos, "W"):
        tcount+=1
    if tcount == 3:
        direc = "T"

    elif Game.checkClear(pos, "N") and Game.checkClear(pos, "S"):
        direc = ("N", "S")
    elif Game.checkClear(pos, "N") and Game.checkClear(pos, "E"):
        direc = ("N, E")
    elif Game.checkClear(pos, "N") and Game.checkClear(pos, "W"):
        direc = ("N", "W")
    elif Game.checkClear(pos, "S") and Game.checkClear(pos, "E"):
        direc = ("S", "E")
    elif Game.checkClear(pos, "S") and Game.checkClear(pos, "W"):
        direc = ("S", "W")
    elif Game.checkClear(pos, "E") and Game.checkClear(pos, "W"):
        direc = ("E", "W")
    elif Game.checkClear(pos, "N"):
        direc = "N"
    elif Game.checkClear(pos, "S"):
        direc = "S"
    elif Game.checkClear(pos, "W"):
        direc = "W"
    elif Game.checkClear(pos, "E"):
        direc = "E"
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