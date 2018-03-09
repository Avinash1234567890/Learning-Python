#!/usr/bin/env python3
import numpy as np
import random
import translate as trans

def spin(percent):
    rand = random.randint(1,100)

    if(rand =< percent[0]):
        return 0
    elif(rand =< percent[0]+percent[1]):
        return 1
    elif(rand =< percent[0]+percent[1]+percent[2]):
        return 2
    else:
        return "error"

move = input("Enter move(rock,paper,or scissors): ")

move = trans.str_to_num(move)

add_move(move)

choice = spin(calc_freq())
print(arb(move,choice))
