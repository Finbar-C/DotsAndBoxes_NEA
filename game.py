class Game():

    def __init__(self, dims: tuple, pnum: int, names: tuple):
        self.__board = Board(dims[0], dims[1])
        players = []
        for i in range(pnum):
            x = Player(names[i])
            players.append(x)

    def place(self, pos, dir):
        pass

class Board():

    EMPTY = " "
    LINE_H = "-"
    LINE_V = "|"

    def __init__(self, rows: int, cols: int):
        self.__grid = [[(None, None, None, None) for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols
    
    def __repr__(self):
        for i in range(self.__rows):
            row = ""
            for j in range(self.__cols):
                row += ". "
            row += ".\n"
            row += "  " for _ in range(self.__cols)
            
            

class Player():
    def __init__(self, name):
        self.__name = name

