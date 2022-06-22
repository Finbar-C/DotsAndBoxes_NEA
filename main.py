from UI import *
from sys import argv

def usage():
    print(f"""
Usage: {argv[0]} [g | t]
g: play with GUI
t: play with Terminal""")
    quit()


if __name__ == "__main__":
    if len(argv) != 2:
        usage()
    elif argv[1] == "t":
        game = Terminal()
    elif argv[1] == "g":
        game = GUI()
    else:
        usage()
    
    game.run()
