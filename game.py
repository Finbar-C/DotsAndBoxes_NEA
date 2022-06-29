from UI import *


class Board():

    EMPTY = "  "
    H_LINE = "--"
    V_LINE = "|"

    def __init__(self, rows: int, cols: int):
        self.__grid = [[(Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY) for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols
    
    def __repr__(self):
        for boxx in range(self.__rows):
            for boxy in range(self.__cols):
                pass
            #go box by box, check each side
    
    def checkBox(self, pos: tuple):
        for i in range(4):
            if (self.__grid[pos[0]][pos[1]])[i] == Board.EMPTY:
                return False
        return True
    
    def directionConvert(self, dir:str):
        if dir.upper() == "N":
            return 0
        elif dir.upper() == "S":
            return 1
        elif dir.upper() == "E":
            return 2
        elif dir.upper() == "W":
            return 3
    
    def checkClear(self, pos: tuple, dir: str):
        dir = Board.directionConvert(dir)
        if (self.__grid[pos[0]][pos[1]])[dir] == Board.EMPTY:
            return True
        return False
    
    def place(self, pos: tuple, dir: str):
        dir = Board.directionConvert(dir)
        if dir <= 1:
            (self.__grid[pos[0]][pos[1]])[dir] = Board.H_LINE
        elif dir >= 2:
            (self.__grid[pos[0]][pos[1]])[dir] = Board.V_LINE



            
            

class Player():
    def __init__(self, name: str):
        self.__name = name
        self.__claimedBoxes = 0
    
    def addBox(self):
        self.__claimedBoxes += 1
    
    @property
    def getName(self):
        return self.__name

if __name__ == "__main__":
    game = Terminal()
    game.run()

class Game():

    def __init__(self, dims: tuple, pnum: int, names: tuple):
        self.__board = Board(dims[0], dims[1])
        self.players = []
        for i in range(pnum):
            x = Player(names[i])
            self.players.append(x)
        self.__turn = 0
    
    @property
    def getTurn(self):
        return self.__turn

    def place(self, pos: tuple, dir: str):
        if self.__board.checkClear(pos, dir):
            self.__board.place(pos, dir)
        

    def __repr__(self):
        return str(self.__board)
    
    def End(self):
        pass

    def nextTurn(self):
        pass

