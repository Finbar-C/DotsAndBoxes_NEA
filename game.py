from UI import *

class Game():

    def __init__(self, dims: tuple, pnum: int, names: tuple):
        self.__board = Board(dims[0], dims[1])
        players = []
        for i in range(pnum):
            x = Player(names[i])
            players.append(x)

    def place(self, pos, dir):
        pass

    def __repr__(self):
        return str(self.__board)

class Board():

    EMPTY = "  "
    LINE_H = "--"
    LINE_V = "|"

    def __init__(self, rows: int, cols: int):
        self.__grid = [[(Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY) for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols
    
    def __repr__(self):
        for boxx in range(self.__rows):
            for boxy in range(self.__cols):
                pass
            #go box by box, check each side
            
            

class Player():
    def __init__(self, name):
        self.__name = name

if __name__ == "__main__":
    game = Terminal()
    game.run()