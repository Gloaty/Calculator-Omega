#This application will be an all in one TBI calculator

#imports
import sys
from calc import *

#main
def intro():
    print("Welcome to Calculator Omega Beta")
    print("This application will be an all in one TBI calculator. ")
    print("This application is still in its beta phase, so please excuse any bugs or lack of features.")
    main()

def main():
    cmd = input("Enter a command: ")
    if cmd == "help":
        print("The following commands are available: ")
        print("help - Displays this message")
        print("quit / exit - Exits the application")
        print("calc - Starts the calculator")
    if cmd == "calc":
        calc()
    if cmd != "exit" or "quit":
        main()
    if cmd == "exit" or cmd == "quit":
        sys.exit()