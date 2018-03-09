#!/usr/bin/env python3

def translate(num):
    if(num == 0):
        return "rock"
    elif (num == 1):
        return "paper"
    elif (num == 2):
        return "scissors"
    else:
        raise ValueError("The value entered was not between 0 and 2")