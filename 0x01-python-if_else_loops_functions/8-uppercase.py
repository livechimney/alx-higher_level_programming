#!/usr/bin/python3
def uppercase(input_string):
    uppercase_string = ""
    for char in input_string:
        if char.islower():
            uppercase_string += char.upper()
        else:
            uppercase_string += char
    print(uppercase_string)

