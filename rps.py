#!/usr/bin/env python3
import numpy as np
import random
import translate as trans

def spin(percent):
    rand = random.randint(1,100)

    if rand =< percent["rock"]:
        return "rock"
    elif rand =< percent["rock"]+percent["paper"]:
        return "paper"
    elif: rand =< percent["rock"]+percent["paper"]+percent["scissors"]:
        return "scissors"
    else:
        return "error"

move = input("Enter move(rock,paper,or scissors): ")

move = trans.str_to_num(move)

add_move(move)

choice = spin(calc_freq())
print(arb(move,choice))
