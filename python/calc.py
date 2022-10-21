#imports
import math
from fractions import Fraction
import decimal

#calculator
def calc():
    def constantResolve(x, y):
        #pi resolver
        if y == "pi":
            y = 3.141592654
            return y
        if x == "pi":
            x = 3.141592654
            return x
        #euler / e resolver
        if y == "e":
            y = 2.718281828
            return y
        if x == "e":
            x = 2.718281828
            return x
    def add(x, y):
        z = int(x) + int(y)
        print(x, "+", y, "=", z)
        return
    def sub(x, y):
        z = int(x) - int(y)
        print(x, "-", y, "=", z)
        return
    def mul(x, y):
        z = int(x) * int(y)
        print(x, "*", y, "=", z)
    def main():
        op = input("Enter an operation: ")
        if op == "help":
            print("add - Adds two numbers together")
            print("sub - Subtracts two numbers")
            print("mul - Multiplies two numbers")
            print("div - Divides two numbers")
            print("sqrt - Finds the square root of a number")
        if op == "add":
            x = input("Number A: ")
            y = input("Number B: ")
            x = constantResolve(x, y)
            add(x, y)
        if op == "sub":
            x = input("Number A: ")
            y = input("Number B: ")
            constantResolve(x, y)
            sub(x, y)
        if op == "mul":
            x = input("Number A: ")
            y = input("Number B: ")
            constantResolve(x, y)
            mul(x, y)
        main()
    main()
    return
calc()
