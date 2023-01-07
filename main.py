from UI import *
from sys import argv

def usage():
    print(f"""
Usage: {argv[0]} [g | t]
g: play with GUI
t: play with Terminal""")
    quit()

def main():
    if len(argv) == 2 and argv[1] not in ("t", "g"):
        usage()
    elif len(argv) == 2:
        if argv[1] == "t":
            game = Terminal()
        elif argv[1] == "g":
            game = GUI()
    elif len(argv) > 2:
        usage()
    else:
        game = GUI()
    
    
    game.run()


if __name__ == "__main__":
    main()