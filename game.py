


class Board():

    EMPTY = "  "
    H_LINE = "--"
    V_LINE = "|"

    #############################################
    #                                           #
    # Skill Set A - List Operations             #
    # Creation, editing and data extraction from#
    # multi-dimensional list                    #
    #                                           #
    #############################################

    def __init__(self, rows: int, cols: int):
        self.__grid = [[[Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY] for _ in range(cols)] for _ in range(rows)]
        self.__claimed = [[Board.EMPTY for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols

    def __repr__(self):
        display = []
        for row in range(self.__rows):
            dRow1 = []
            dRow2 = []
            for col in range(self.__cols):
                dRow1.append(".")
                dRow1.append(self.__grid[row][col][0])
                dRow2.append(self.__grid[row][col][2])
                if self.__claimed[row][col] == Board.EMPTY:
                    dRow2.append(Board.EMPTY)
                else:
                    dRow2.append(str(self.__claimed[row][col]) + " ")
            col = self.__cols - 1
            dRow1.append(".")
            dRow1.append("\n")
            dRow2.append(self.__grid[row][col][3])
            dRow2.append("\n")
            display += dRow1
            display += dRow2
        row = self.__rows - 1
        dRow = []
        for col in range(self.__cols):
            dRow.append(".")
            dRow.append(self.__grid[row][col][1])
            dRow.append(".")
        display += dRow
        ReturnStr = ""
        for i in range(len(display)):
            ReturnStr += display[i]
        return ReturnStr
                    
            #go box by box, check each side
    
    
    def getBoxExists(self, pos: tuple):
        if self.__claimed[pos[0]][pos[1]] == Board.EMPTY:
            return -1
        return self.__claimed[pos[0]][pos[1]]
    
    def directionConvert(self, dir:str):
        if dir.upper() == "N":
            return 0
        elif dir.upper() == "S":
            return 1
        elif dir.upper() == "E":
            return 2
        elif dir.upper() == "W":
            return 3
    
    def getDataPoint(self, row, col, dir):
        dir = self.directionConvert(dir)
        if self.__grid[row][col][dir] == Board.EMPTY:
            return 0
        return 1
    
    def checkLine(self, pos: tuple, dir: int):
        if (self.__grid[pos[0]][pos[1]])[dir] == Board.EMPTY:
            return False
        return True

    def checkBox(self, pos: tuple):
        for i in range(4):
            if not self.checkLine(pos, i):
                return False
        return True
     
    def CheckFull(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if not self.checkBox((i, j)):
                    return False
        return True
    
    def checkClear(self, pos: tuple, dir: str):
        dir = self.directionConvert(dir)
        if self.__grid[pos[0]][pos[1]][dir] == Board.EMPTY:
            return True
        return False
    
    def place(self, pos: tuple, dir: str):
        dir = self.directionConvert(dir)
        if dir <= 1:
            self.__grid[pos[0]][pos[1]][dir] = Board.H_LINE
        elif dir >= 2:
            self.__grid[pos[0]][pos[1]][dir] = Board.V_LINE
    
    def MatchedPlace(self, pos: tuple, dir: str):
        dir = self.directionConvert(dir)
        if dir == 0:
            if pos[0] - 1 >= 0:
                return pos[0] - 1, pos[1], "S"
        elif dir == 1:
            if pos[0] + 1 < self.__rows:
                return pos[0] + 1, pos[1], "N"
        elif dir == 2:
            if pos[1] + 1 < self.__cols:
                return pos[0], pos[1] + 1, "W"
        elif dir == 3:
            if pos[1] - 1 >= 0:
                return pos[0], pos[1] - 1, "E"
    # match up placement to equivalent place in neighbouring box

    def ClaimBox(self, pos: tuple, pnum: int):
        self.__claimed[pos[0]][pos[1]] = pnum
    
    def getScores(self, numPlayers: int):
        scores = [0 for _ in range(numPlayers)]
        for i in range(self.__rows):
            for j in range(self.__cols):
                scores[(self.__claimed[i][j])] += 1
        return scores



            
            

class Player():
    def __init__(self, name: str):
        self.__name = name
        self.__claimedBoxes = 0
    
    def addBox(self):
        self.__claimedBoxes += 1
    
    @property
    def getName(self):
        return self.__name

class Game():

    def __init__(self, dims: tuple, pnum: int, names: list):
        self.__board = Board(dims[0], dims[1])
        self.players = []
        for i in range(pnum):
            x = Player(names[i])
            self.players.append(x)
        self.__turn = 0
    
    def getDataPoint(self, row, col, dir):
        return self.__board.getDataPoint(row, col, dir)

    def checkClear(self, pos: tuple, dir: str):
        return self.__board.checkClear(pos, dir)

    def getTurn(self):
        return self.__turn
    
    def getBoxExists(self, pos: tuple):
        return self.__board.getBoxExists(pos)

    def place(self, pos: tuple, dir: str):
        boxCreated = False
        if self.__board.checkClear(pos, dir):
            self.__board.place(pos, dir)
            res = self.__board.MatchedPlace(pos, dir)
            if res != None:
                newPos = (res[0], res[1])
                newDir = res[2]
                self.__board.place(newPos, newDir)
                if self.__board.checkBox(newPos):
                    self.__board.ClaimBox(newPos, self.__turn)
                    boxCreated = True
        if self.__board.checkBox(pos):
            self.__board.ClaimBox(pos, self.__turn)
            boxCreated = True
        
        return boxCreated
        

    def __repr__(self):
        return str(self.__board)
    
    def End(self):
        if self.__board.CheckFull():
            return True
        return False
    
    def CalculateScores(self):
        scores = self.__board.getScores(len(self.players))
        return scores

    def nextTurn(self):
        if self.__turn + 1 < len(self.players):
            self.__turn += 1
        elif self.__turn +1 == len(self.players):
            self.__turn = 0


