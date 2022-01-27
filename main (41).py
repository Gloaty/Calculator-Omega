#this program will be an all-in-one calculator

#imports
import math
import time

#welcome
print("Welcome to Calculator Ωmega!")
time.sleep(1)
number_count = int(input("Please input required amount of integers: "))
operation_choice = input("Please input required operator: (+, -, *, /, %, **) ")

#addition
if operation_choice == "+" and number_count == "2":
    first = int(input("First: "))
    second = int(input("Second: "))
    sum = int(first) + int(second)
    print(sum)