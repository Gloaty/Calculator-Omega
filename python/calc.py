#imports
import math

#global variables
global op, x, y, history

#calculator
def calc():
    def add(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x + y
        print(z)
        history = z
        return
    def sub(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x - y
        print(z)
        history = z
        return
    def mul(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x * y
        print(z)
        history = z
        return
    def div(x, y):
        x = input("Number A: ")
        y = input("Number B: ")
        z = x / y
        print(z)
        history = z
        return
    def srqt(x):
        x = input("Number: ")
        if x <= 0:
            print("Math ERROR")
            pass
        z = math.sqrt(x)
        print(z)
        history = z
        return
    def rndm(x, y):
        print("coin - Flip a coin")
        print("dice - Roll a dice")
        prind("rndm - Random number between 1 and selected number. ")
    def main():
        op = input("Enter an operation: ")
        if op == "help":
            print("add - Adds two numbers together")
            print("sub - Subtracts two numbers")
            print("mul - Multiplies two numbers")
            print("div - Divides two numbers")
            print("sqrt - Finds the square root of a number")
            print("rndm - Randomness Engine")
        if op == "add":
            add()
        return
    main()
    return
main()