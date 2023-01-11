
from game import *
from accounts import *
from tkinter import *
from itertools import product
from abc import ABC, abstractmethod
from AI import Move
from functools import partial

class UI():

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal(UI):
    def __init__(self):
        self.__game = Game((4,4), 2, ("1", "2"), ["P", "P"])
    
    def run(self):
        self.play()
    
    def __repr__(self):
        pass

    def place(self):
        valid = [1, 2, 3, 4]
        while True:
            row = int(input("What is the Row Number for your box? "))
            if row in valid:
                break
            else:
                print("Valid options are numbers 1-4")
        while True:
            col = int(input("What is the Column Number for your box? "))
            if col in valid:
                break
            else:
                print("Valid options are numbers 1-4")
        pos = (row-1, col-1)
        valRef = ["N", "S", "E", "W"]
        while True:
            direction = input("Which side of the box would you like to play (N, S, E or W)? ")
            if direction.upper() in valRef:
                break
            else:
                print("Valid directions are N, S, E and W")
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
        Button(frame, text="Play Multiplayer", command=self.__NewGame).pack(fill=X)
        Button(frame, text="Play vs AI", command=self.__AiGame).pack(fill=X)
        Button(frame, text="Options", command=self.__Settings).pack(fill=X)
        Button(frame, text="Exit", command=self.__Exit).pack(fill=X)

        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width = 50)
        scroll.pack(side=RIGHT, fill = Y)
        console.pack(side=LEFT, fill = Y)
        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        self.__console = console
        self.__Names = []
        self.__loggedIn = False
        self.__activeAccountName = None

    def getEntryData(self, entry):
        return entry.get()

    
    def run(self):
        self.__root.mainloop()
    
    def __AiGame(self):
        self.__NewGamewindow = Toplevel(self.__root)
        self.__NewGamewindow.title("AI Game Creation Menu")
        frame = Frame(self.__NewGamewindow)
        frame.pack()
        Label(frame, text="Width:").grid(row=0, column=0, padx=5, pady=5)
        self.__width = Entry(frame)
        self.__width.grid(row=0, column=1, pady=5, padx=5)
        Label(frame, text="Height:").grid(row=1, column=0, padx=5, pady=5)
        self.__height = Entry(frame)
        self.__height.grid(row=1, column=1, pady=5, padx=5)
        Label(frame, text="Difficulty:").grid(row=2, columnspan=2, padx=5, pady=5)
        Button(frame, text="Random", command=self.__random).grid(row=3, column=0, padx=5, pady=5, columnspan=1)
        Button(frame, text="Easy", command=self.__easy).grid(row=3, column=1, padx=5, pady=5, columnspan=1)
        Button(frame, text="Medium", command=self.__medium).grid(row=4, column=0, padx=5, pady=5, columnspan=1)
        Button(frame, text="Difficult", command=self.__difficult).grid(row=4, column=1, padx=5, pady=5, columnspan=1)

    def __random(self):
        self.__NumPlayers = 2
        if not self.__loggedIn:
            self.__Names = ["Player", "RandomAI"]
        else:
            self.__Names = [self.__activeAccountName, "RandomAI"]
        self.__types = ["P", "C0"]
        self.__GameWin()


    def __easy(self):
        self.__NumPlayers = 2
        if not self.__loggedIn:
            self.__Names = ["Player", "EasyAI"]
        else:
            self.__Names = [self.__activeAccountName, "EasyAI"]
        self.__types = ["P", "C1"]
        self.__GameWin()

    def __medium(self):
        self.__NumPlayers = 2
        if not self.__loggedIn:
            self.__Names = ["Player", "MediumAI"]
        else:
            self.__Names = [self.__activeAccountName, "MediumAI"]
        self.__types = ["P", "C2"]
        self.__GameWin()

    def __difficult(self):
        self.__NumPlayers = 2
        if not self.__loggedIn:
            self.__Names = ["Player", "DifficultAI"]
        else:
            self.__Names = [self.__activeAccountName, "DifficultAI"]
        self.__types = ["P", "C3"]
        self.__GameWin()

    def __NewGame(self):
        self.__NewGamewindow = Toplevel(self.__root)
        self.__NewGamewindow.title("Multiplayer Game Creation Menu")
        frame = Frame(self.__NewGamewindow)
        frame.grid(row=0,column=0)
        Label(frame, text="Width:").grid(row=0, column=0, padx=5, pady=5)
        self.__width = Entry(frame)
        self.__width.grid(row=0, column=1, pady=5, padx=5)
        Label(frame, text="Height:").grid(row=1, column=0, padx=5, pady=5)
        self.__height = Entry(frame)
        self.__height.grid(row=1, column=1, pady=5, padx=5)
        Label(frame, text="Number of Players:").grid(row=2, column=0, padx=5, pady=5)
        self.numPlayersEntry = Entry(frame)
        self.numPlayersEntry.grid(row=2, column=1, padx=5, pady=5)
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
        self.__NumPlayers = int(self.getEntryData(self.numPlayersEntry))
        self.__NamesEntries = []
        self.__types = []
        window = Toplevel(self.__NewGamewindow)
        frame = Frame(window)
        frame.pack()
        for i in range(self.__NumPlayers):
            Label(frame, text=f"Name for Player {i+1}").grid(row=i, column=0, padx=5, pady=5)
            self.__NamesEntries.append(Entry(frame))
            self.__NamesEntries[i].grid(row=i, column=1, padx=5, pady=5)
            self.__types.append("P")
        Button(frame, text="Confirm", command=self.__GameWin).grid(row=len(self.__NamesEntries), columnspan=2, padx=5, pady=5)        

    #make an netry for each player
    #add player names to list
    #create list of player initials from player[i][0]
    #start game with given number of players
    #claim box with player initial
    #add colour later

    def __Place(self, row, col, dir):
        pos = (row, col)
        bc = self.__Game.place(pos, dir)
        return bc


    def __PlayTurn(self, row, col, direction):
        turn = self.__Game.getTurn()
        row = row
        col = col
        direc = direction

        validU = ["top", "t", "charm", "up", "north", "n"]
        validL = ["left", "l", "west", "w"]
        validR = ["right", "r", "east", "e"]
        validD = ["bottom", "b", "strange", "down", "south", "s"]
        #take data from buttons to give to place. use true / false return to decide on try again and turn cont.
        direc = direc.lower()
        if direc not in validU and direc not in validL and direc not in validR and direc not in validD:
            return
        if direc in validU:
            if not self.__Game.checkClear((row, col), "N"):
                return
            bc = self.__Place(row, col, "N")
            direc = "N"
        elif direc in validL:
            if not self.__Game.checkClear((row, col), "W"):
                return
            bc = self.__Place(row, col, "W")
            direc = "W"
        elif direc in validR:
            if not self.__Game.checkClear((row, col), "E"):
                return
            bc = self.__Place(row, col, "E")
            direc = "E"
        elif direc in validD:
            if not self.__Game.checkClear((row, col), "S"):
                return
            bc = self.__Place(row, col, "S")
            direc = "S"
        
        if direc == "N":
            self.__boxes[row][col][2].config(bg="black")
            self.__boxes[row][col][2].grid(row=0, column = 1, padx = 1, pady = 1)
        elif direc == "W":
            self.__boxes[row][col][3].config(bg="black")
            self.__boxes[row][col][3].grid(row=1, column=0, padx = 1, pady = 1)
        else:
            if direc == "E" and col + 1 == self.__width:
                self.__boxes[row][col][6].config(bg="black")
                self.__boxes[row][col][6].grid(row=1,column=2, padx=1, pady=1)
            elif direc == "S" and row + 1 == self.__height:
                self.__boxes[row][col][8].config(bg="black")
                self.__boxes[row][col][8].grid(row=2,column=1, padx=1, pady=1)
            else:
                if direc == "E":
                    self.__boxes[row][col+1][3].config(bg="black")
                    self.__boxes[row][col+1][3].grid(row=1,column=0, padx=1, pady=1)
                elif direc == "S":
                    self.__boxes[row+1][col][2].config(bg="black")
                    self.__boxes[row+1][col][2].grid(row=0,column=1, padx=1, pady=1)

        if bc:
            if self.__Game.getBoxExists((row, col)) != -1:
                self.__boxes[row][col][4].config(text=f"      \n  {self.__Names[self.__getTurn()][0]}   \n      ")
                self.__boxes[row][col][4].grid(row=1,column=1, padx=1, pady=1)
            if col+1 != self.__width:
                if self.__Game.getBoxExists((row, col+1)) != -1 and direc == "E" and col+1 != self.__width:
                    self.__boxes[row][col+1][4].config(text=f"      \n  {self.__Names[self.__getTurn()][0]}   \n      ")
                    self.__boxes[row][col+1][4].grid(row=1,column=1, padx=1, pady=1)
            if row+1 != self.__height:
                if self.__Game.getBoxExists((row+1, col)) != -1 and direc == "S" and row+1 != self.__height:
                   self.__boxes[row+1][col][4].config(text=f"      \n  {self.__Names[self.__getTurn()][0]}   \n      ")
                   self.__boxes[row+1][col][4].grid(row=1,column=1, padx=1, pady=1)
            if self.__Game.getBoxExists((row, col-1)) != -1 and direc == "W" and col != 0:
                self.__boxes[row][col-1][4].config(text=f"      \n  {self.__Names[self.__getTurn()][0]}   \n      ")
                self.__boxes[row][col-1][4].grid(row=1,column=1, padx=1, pady=1)
            if self.__Game.getBoxExists((row-1, col)) != -1 and direc == "N" and row != 0:
                self.__boxes[row-1][col][4].config(text=f"      \n  {self.__Names[self.__getTurn()][0]}   \n      ")
                self.__boxes[row-1][col][4].grid(row=1,column=1, padx=1, pady=1)

        if not self.__Game.End():
            if not bc:
                self.__Game.nextTurn()
            x = self.__getTurn()
            self.__currentplayer = self.__Names[x]
            self.__turndisplay.config(text=f"Current player is {self.__currentplayer}")
            self.__turndisplay.grid(row=0, columnspan=3)
            if self.__Game.players[x].getType() == "C":
                move = Move(self.__Game.players[x].getDifficulty(), self.__Game)
                self.__PlayTurn(move[0], move[1], move[2])
        else:
            self.__EndGame()
        return

    def __EndGame(self):
        self.__GameEndWindow = Toplevel(self.__GameWindow)
        self.__GameEndWindow.title("Results")
        frame = Frame(self.__GameEndWindow)
        frame.pack()
        scores = self.__Game.CalculateScores()
        winner = -1
        maximum = 0
        for i in range(len(scores)):
            if scores[i] > maximum:
                winner = i
                maximum = scores[i]
        Label(frame, text=f"{self.__Names[winner]} won with {maximum} claimed squares!").pack()
        Button(frame, text="Return to Menu", command=self.__EndGameDestroy).pack()
    
    def __EndGameDestroy(self):
        self.__GameWindow.destroy()

    def __getTurn(self):
        return self.__Game.getTurn()

    def __GameWin(self):
        width = int(self.__width.get())
        self.__width = width
        height = int(self.__height.get())
        self.__height = height
        numPlayers = int(self.__NumPlayers)
        
        if len(self.__Names) == 0:
            self.__Names = []
            for i in range(numPlayers):
                self.__Names.append(self.__NamesEntries[i].get())

        self.__Game = Game((width, height), numPlayers, self.__Names, self.__types)
        self.__GameWindow = Toplevel(self.__root)
        self.__GameWindow.title("Game Window")
        self.__currentplayer = self.__Names[0]
        topframe = Frame(self.__GameWindow)


        topframe.pack(padx=15, pady=15)
        self.__NewGamewindow.destroy()
        gridframe = Frame(topframe)
        gridframe.grid(row=0, column=0)
        self.__boxes = [[] for _ in range(height)]
        for i in range(width):
            for j in range(height):
                frame = []
                frame.append(Frame(gridframe))
                self.__boxes[j].append(frame)
                self.__boxes[j][i][0].grid(row=j,column=i) # frame item at 0, corner 1, top 2, left 3, centre 4, right and bottom edges follow on edge self.__boxes
                self.__boxes[j][i].append(Label(self.__boxes[j][i][0], text=" ", bg="black"))
                self.__boxes[j][i][1].grid(row=0,column=0, padx=1, pady=1)
                self.__boxes[j][i].append(Button(self.__boxes[j][i][0], text="       ", bg="grey", command=partial(self.__PlayTurn, j, i, "N")))
                self.__boxes[j][i][2].grid(row=0,column=1, padx=1, pady=1)
                self.__boxes[j][i].append(Button(self.__boxes[j][i][0], text=" \n \n ", bg="grey", command=partial(self.__PlayTurn, j, i, "W")))
                self.__boxes[j][i][3].grid(row=1,column=0, padx=1, pady=1)
                self.__boxes[j][i].append(Label(self.__boxes[j][i][0], text="      \n      \n      ", bg="white"))
                self.__boxes[j][i][4].grid(row=1,column=1, padx=1, pady=1)
                if i+1 == width:
                    self.__boxes[j][i].append(Label(self.__boxes[j][i][0], text=" ", bg="black"))
                    self.__boxes[j][i][5].grid(row=0,column=2, padx=1, pady=1)
                    self.__boxes[j][i].append(Button(self.__boxes[j][i][0], text=" \n \n ", bg="grey", command=partial(self.__PlayTurn, j, i, "E")))
                    self.__boxes[j][i][6].grid(row=1,column=2, padx=1, pady=1)
                else:
                    self.__boxes[j][i].append(None)
                    self.__boxes[j][i].append(None)
                if j+1 == height:
                    self.__boxes[j][i].append(Label(self.__boxes[j][i][0], text=" ", bg="black"))
                    self.__boxes[j][i][7].grid(row=2,column=0, padx=1, pady=1)
                    self.__boxes[j][i].append(Button(self.__boxes[j][i][0], text="      ", bg="grey", command=partial(self.__PlayTurn, j, i, "S")))
                    self.__boxes[j][i][8].grid(row=2,column=1, padx=1, pady=1)
                else:
                    self.__boxes[j][i].append(None)
                    self.__boxes[j][i].append(None)
                if i+1 == width and j+1 == height:
                    self.__boxes[j][i].append(Label(self.__boxes[j][i][0], text=" ", bg="black"))
                    self.__boxes[j][i][9].grid(row=2,column=2, padx=1, pady=1)
                else:
                    self.__boxes[j][i].append(None)
        buttonframe = Frame(topframe)
        buttonframe.grid(row=1, column=0)
        self.__turndisplay = Label(buttonframe, text=f"Current player is {self.__currentplayer}")
        self.__turndisplay.grid(row=0, columnspan=3)
        Button(buttonframe, text="Exit", command=self.__GameWindow.destroy).grid(row=1,column=2, padx=5, pady=5)
        Button(buttonframe, text="Help", command=self.__showHelpGame).grid(row=1, column=0, padx=5, pady=5)

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
    
    def __showHelpGame(self):
        pass

    def __Exit(self):
        self.__root.quit()




if __name__ == "__main__":
    game = Terminal()
    game.run()
