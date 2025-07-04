#!/usr/bin/env python3

def add_one(x):
    x = x + 1
    print(f"With methode 'add_one': {x}")

number = 5
print(f"Before add_one: {number}")

add_one(number)

print(f"After add_one: {number}")
