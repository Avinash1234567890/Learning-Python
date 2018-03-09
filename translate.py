#!/usr/bin/env python3

def num_to_str(num):
    if(int(num) == 0):
        return "rock"
    elif (int(num) == 1):
        return "paper"
    elif (int(num) == 2):
        return "scissors"
    else:
        raise ValueError(num)

def str_to_num(str):
    if (str(str) == "rock"):
        return 0
    elif (str(str) == "paper"):
        return 1
    elif (str(str) == "scissors"):
        return 2
    else:
        raise ValueError(str)