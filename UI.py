
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

            self.playTurn()
    
    def playTurn(self):
        print(self.__game)
        cont = self.place()
        if cont == True:
            self.playTurn()
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
        self.__NewGamewindow = Toplevel(self.__root)
        self.__NewGamewindow.title("Game Creation Menu")
        frame = Frame(self.__NewGamewindow)
        frame.grid(row=0,column=0)
        Label(frame, text="Width:").grid(row=0, column=0, padx=5, pady=5)
        self.__width = Entry(frame).grid(row=0, column=1, pady=5, padx=5)
        Label(frame, text="Height:").grid(row=1, column=0, padx=5, pady=5)
        self.__height = Entry(frame).grid(row=1, column=1, pady=5, padx=5)
        Label(frame, text="Number of Players:").grid(row=2, column=0, padx=5, pady=5)
        self.__numPlayersEntry = Entry(frame).grid(row=2, column=1, padx=5, pady=5)
        Label(frame, text="Walls?").grid(row=3, column=0, padx=5, pady=5)
        self.__walls_var = False
        self.__walls_switch = Button(frame, text="Off", bg="grey", fg="red", command=self.walls_toggle)
        self.__walls_switch.grid(row=3, column=1, padx=5, pady=5)
        Button(frame, text="Create New Game", command=self.__GetNames).grid(row=4, columnspan=2, padx=5, pady=5)



    def walls_toggle(self): #switch method 
        if not self.__walls_var:
            self.__walls_switch.config(text="on", bg="white", fg="green")
            self.__walls_var = True
        if self.__walls_var:
            self.__walls_switch.config(text="Off", bg="grey", fg="red")
            self.__walls_var = False

    def __Settings(self):
        # displays settings window
        window = Toplevel(self.__root)
        window.title("Settings Menu")
        frame = Frame(window)
        #add options
        frame.pack()

    def __GetNames(self):
        window = Toplevel(self.__NewGamewindow)
        frame = Frame(window)
        frame.pack()
        self.__NumPlayers = self.__numPlayersEntry.get()
        self.__NamesEntries = []
        for i in range(self.__NumPlayers):
            Label(frame, text=f"Name for Player {i}").grid(row=i, column=0, padx=5, pady=5)
            self.__NamesEntries.append(Entry(frame).grid(row=i, column=1, padx=5, pady=5))
        Button(frame, text="Confirm", command=self.__GameWin).grid(row=len(self.__NamesEntries), columnspan=2, padx=5, pady=5)        

    #make an netry for each player
    #add player names to list
    #create list of player initials from player[i][0]
    #start game with given number of players
    #claim box with player initial
    #add colour later

    def __Place(self, row, col):
        pass

    def __PlayTurn(self):
        pass
        #take data from buttons to give to place. use true / false return to decide on try again and turn cont.


    def __GameWin(self):
        width = int(self.__width.get())
        height = int(self.__height.get())
        numPlayers = int(self.__NumPlayers)
        Names = []
        for i in range(numPlayers):
            Names.append(self.__NamesEntries[i].get())
        self.__Game = Game((width, height), numPlayers, Names)
        self.__GameWindow = Toplevel(self.__root)
        self.__root.title("Game Window")
        frame = Frame(self.__GameWindow)

        frame.pack()

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
