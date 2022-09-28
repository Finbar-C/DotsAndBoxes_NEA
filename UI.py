
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

def walls_toggle(): #switch method 
    global on_var
    if not var:
        walls_switch.config(text="on", bg="white", fg="green")
        var = True
    if var:
        walls_switch.config(text="Off", bg="grey", fg="red")
        var = False


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
        window = Toplevel(self.__root)
        window.title("Game Creation Menu")
        frame = Grid()
        
        Label(frame, text="Width:").grid(row=0, column=0, padx=5, pady=5)
        Entry(frame).grid(row=0, column=1, pady=5, padx=5)
        Label(frame, text="Height:").grid(row=1, column=0, padx=5, pady=5)
        Entry(frame).grid(row=1, column=1, pady=5, padx=5)
        Label(frame, text="Walls?").grid(row=2, column=0, padx=5, pady=5)
        walls_var = False
        walls_switch = Button(frame, text="Off", bg="grey", fg="red", command=walls_toggle)
        walls_switch.grid(row=2, column=1, padx=5, pady=5)
        Button(frame, text="Create New Game", command=self.__GameWin).grid(row=3, columnspan=2, padx=5, pady=5)

        frame.pack(window)


    def __Settings(self):
        pass # displays settings window

    def __GameWin(self):
        pass # window in which game is played

    def __showHelpMain(self):
        window = Toplevel(self.__root)
        window.title("Dots and Boxes - Help")
        frame = Frame(window)
        Label(frame, text="Filler Text Until I Figure Out What To Write in The Help Window").pack()

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
