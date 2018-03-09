#!/usr/bin/env python3

def num_to_str(move):
    if(int(move) == 0):
        return "rock"
    elif (int(move) == 1):
        return "paper"
    elif (int(move) == 2):
        return "scissors"
    else:
        raise ValueError(move)

def str_to_num(move):
    if (str(move) == "rock"):
        return 0
    elif (str(move) == "paper"):
        return 1
    elif (str(move) == "scissors"):
        return 2
    else:
        raise ValueError(move)