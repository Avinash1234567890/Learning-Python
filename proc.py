#!/usr/bin/env python3

from cycle import * 

def calc_freq(move_list):
    count = [0, 0, 0]

    for move in move_list:
        count[move] += 1
    return count

def arb(player_move, machine_move):
    if(cycle(player_move, 1, 3) == machine_move):
        return {
            "winner": "player",
            "winning move": player_move,
            "loosing move": machine_move
        }
    else:
        return {
            "winner": "machine",
            "winning move": machine_move,
            "loosing move": player_move
        }