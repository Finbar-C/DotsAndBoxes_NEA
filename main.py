from UI import *

runWith = None
if __name__ == "__main__":
    if runWith == "t":
        game = Terminal()
    elif runWith == "g":
        game = GUI()
