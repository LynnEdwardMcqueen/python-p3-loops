#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")
    

def square_integers(int_list):
    squared_list = [number * number for number in int_list]
    return squared_list

def fizzbuzz():
    print_val = ""
    for i in range(1,101):
        if (i % 3) == 0:
            print_val ="Fizz"
        if (i % 5) == 0:
            print_val += "Buzz"
        if print_val == "":
            print_val = i
        print(print_val)
        print_val = ""

