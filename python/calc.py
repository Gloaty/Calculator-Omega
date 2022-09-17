#imports
import math

#global variables
global op, x, y

#calculator
def calc():
    def add(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x + y
        print(x, "+", y, "=", z)
        return
    def sub(x, y):
        pass
    def main():
        op = input("Enter an operation: ")
        if op == "help":
            print("add - Adds two numbers together")
            print("sub - Subtracts two numbers")
            print("mul - Multiplies two numbers")
            print("div - Divides two numbers")
            print("sqrt - Finds the square root of a number")
        if op == "add":
            add()
        return
    main()
    return
