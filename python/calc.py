#imports
import math
import time 

#calculator
class calc():
    def add(x, y):
        x = int(input("Number A: "))
        y = int(input("Number B: "))
        z = x + y
        print(z)
        history = z
        return
    def sub():
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
        history = ("√", x, " = ", z)
        return
    def rndm(x, y):
        print("coin - Flip a coin")
        print("dice - Roll a dice")
        print("rndm - Random number between 1 and selected number. ")
    def rcll(history):
        print("Recalling history...")
        time.sleep(1)
        print(history)
        return

def main():
    x = 0
    y = 0
    history = "null"
    op = input("Enter an operation: ")
    if op == "help":
        print("add - Adds two numbers together")
        print("sub - Subtracts two numbers")
        print("mul - Multiplies two numbers")
        print("div - Divides two numbers")
        print("sqrt - Finds the square root of a number")
        print("rndm - Randomness Engine")
        print("rcll - Recall calculation history")
    if op == "add":
        calc.add(x, y)
    if op == "sub":
        calc.sub(x, y)
    if op == "mul":
        calc.mul(x, y)
    if op == "div":
        calc.div(x, y)
    if op == "sqrt":
        calc.sqrt(x)
    if op == "rndm":
        calc.rndm(x, y)
    if op == "rcll":
        calc.rcll(history)
    main()
main()