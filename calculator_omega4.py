#this program will be an all-in-one calculator

#imports
import math
import time
import tkinter
from tkinter import messagebox
#possibly not needed, research needed

#welcome
print("Welcome to Calculator Ωmega!")
time.sleep(1)
number_count = int(input("Please input required amount of integers: (Max: 5) "))

def overFlowCheck():
    if number_count > 5:
        for i in range(1, 10):
            print("// WARNING: CRITICAL ERROR //")
            print("// VARIABLE > 5 //")
            print("// FAILURE IMMINENT //")
            print("// RETRYING //")
            print("----------------------------------")
            time.sleep(2)


#tkinter error message
if number_count > 5:
    messagebox.showerror("ERROR", overFlowCheck())

#welcome continued
operation_choice = input("Please input required operator: (+, -, *, /, %, **) ")

#addition w/ 2 int
if operation_choice == "+" and number_count == "2":
    first = int(input("First: "))
    second = int(input("Second: "))
    local_sum = int(first) + int(second)
    print(local_sum)
