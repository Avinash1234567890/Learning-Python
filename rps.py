#!/usr/bin/env python3
from random import randint
from translate import str_to_num
from proc import calc_freq, arb

move_list = [0, 1, 2]

def add_move(move):
    move_list.append(int(move))

def spin(percent):
    rand = randint(1,100)

    if(rand <= percent[0]):
        return 0
    elif(rand <= percent[0] + percent[1]):
        return 1
    elif(rand <= percent[0] + percent[1] + percent[2]):
        return 2
    else:
        raise Exception()

move = input("Enter move(rock,paper,or scissors): ")

move = str_to_num(move)

add_move(move)

choice = spin(calc_freq(move_list))
result = arb(move,choice)
