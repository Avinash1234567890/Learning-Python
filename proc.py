#!/usr/bin/env python3

from cycle import * 

def calc_freq(move_list):
    count = [0, 0, 0]

    for move in move_list:
        count[move] += 1
    total = 0
    for i in range(len(count)):
        total += count[i]
    percent = []
    for j in range(len(count)):
        frac = float((count[j] / total) * 100)
        percent.insert(j, frac)
    return percent


def arb(player_move, machine_move):
    if(player_move == machine_move):
        return {
            "winner": "draw",
            "winning move": machine_move,
            "loosing move": player_move
        }
    if(cycle(player_move, 1, 2) == machine_move):
        return {
            "winner": "machine",
            "winning move": machine_move,
            "loosing move": player_move
        }
    else:
        return {
            "winner": "player",
            "winning move": player_move,
            "loosing move": machine_move
        }

def choose_move(spun_move):
    result =  cycle(spun_move, 1, 2)
    return result