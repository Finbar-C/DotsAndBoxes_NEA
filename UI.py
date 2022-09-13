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
    
    def run(self):
        self.play()
    
    def __repr__(self):
        pass

    def place(self):
        row = int(input("What is the Row Number for your box? "))
        col = int(input("What is the Column Number for your box? "))
        pos = (row, col)
        direction = input("Which side of the box would you like to play (N, S, E or W)? ")
        cont = self.__game.place(pos, direction)
        return cont

    def play(self):
        while not self.__game.End():

            Terminal.playTurn()
    
    def playTurn(self):
        print(self.__game)
        cont = Terminal.place()
        if cont == True:
            Terminal.playTurn()
        else:
            self.__game.nextTurn()


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
