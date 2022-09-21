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
        frame = Frame(self.__root)
        frame.pack()
        Button(frame, text="Help", command=self.__showHelpMain).pack(fill=X)
        Button(frame, text="New Game", command=self.__NewGame).pack(fill=X)
        Button(frame, text="Options", command=self.__Settings).pack(fill=X)
        Button(frame, text="Exit", command=self.__Exit).pack(fill=X)

        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width = 50)
        scroll.pack(side=RIGHT, fill = Y)
        console.pack(side=LEFT, fill = Y)
        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        self.__console = console


    
    def run(self):
        self.__root.mainloop()

    def __NewGame(self):
        window = Tk()
        window.title("Game Creation Menu")
        frame = Grid(window)

    def __Settings(self):
        pass # displays settings window

    def __GameWin(self):
        pass # window in which game is played

    def __showHelpMain(self):
        window = Tk()
        window.title("Dots and Boxes - Help")
        window = Toplevel(self.__root)
        frame = Frame(window)
        Label(frame, text="Filler Text Until I Figure Out What To Write in The Help Window")

        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill = Y)
        frame.pack(side=LEFT, fill=Y)
        scroll.config(command=frame.yview)
        window.config(yscrollcommand=scroll.set)

    def __Exit(self):
        self.__root.quit()


if __name__ == "__main__":
    game = Terminal()
    game.run()
