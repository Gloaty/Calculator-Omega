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
        print(z)
        return
    def sub(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x - y
        print(z)
    def mul(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x * y
        print(z)
    def div(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x / y
        print(z)
    def srqt(x):
        x = input("Number: ")
        if x <= 0:
            print("Math ERROR")
            pass
        z = math.sqrt(x)
        print(z)
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
main()