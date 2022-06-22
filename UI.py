from game import *
from accounts import *
from tkinter import *
from itertools import product
from abc import ABC, abstractmethod

class UI():

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal():
    def __init__(self):
        self.__game = Game()
    
    def run(self):
        pass

class GUI():
    def __init__(self):
        root = Tk()
        root.title("Dots and Boxes")
    
    def run(self):
        self.__root.mainloop()

class NewGame(GUI):
    pass # displays new game creation window

class Settings(GUI):
    pass # displays settings window


