class Game():
    def __init__(self):
        self.__board = Board()

    def place(self, pos, dir):
        pass

class Board():
    def init(self, rows, cols):
        self.__grid = [[(None, None, None, None) for _ in range(cols)] for _ in range(rows)]

