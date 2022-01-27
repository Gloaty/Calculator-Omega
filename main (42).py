#this program will be an all-in-one calculator

#imports
import math
import time
import tkinter

#welcome
print("Welcome to Calculator Ωmega!")
time.sleep(1)
number_count = int(input("Please input required amount of integers: (Max: 5) "))

def overFlowCheck():
    if number_count > 5:
        for i in range(1, 100):
            print("// WARNING: CRITICAL ERROR //")
            print("// VARIABLE > 5 //")
            print("// FAILURE IMMINENT //")
            print("// RETRYING //")
            print("----------------------------------")
            time.sleep(2)

#tkinter error message
if number_count > 5:
    messagebox.overFlowCheck("ERROR", overFlowCheck, [default])

#welcome continued
operation_choice = input("Please input required operator: (+, -, *, /, %, **) ")

#addition w/ 2 int
if operation_choice == "+" and number_count == "2":
    first = int(input("First: "))
    second = int(input("Second: "))
    sum = int(first) + int(second)
    print(sum)