from game import *
from accounts import *
from tkinter import *
from itertools import product
from abc import ABC, abstractmethod

class UI():

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal(UI):
    def __init__(self):
        self.__game = Game((4,4), 2, ("1", "2"))
    
    def __repr__(self):
        pass

    def run(self):
        print(self.__game)


class GUI(UI):
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Dots and Boxes")
    
    def run(self):
        self.__root.mainloop()

class NewGame(GUI):
    pass # displays new game creation window

class Settings(GUI):
    pass # displays settings window

class GameWin(GUI):
    pass # window in which game is played


if __name__ == "__main__":
    game = Terminal()
    game.run()