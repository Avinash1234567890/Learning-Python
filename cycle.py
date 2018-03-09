#!/usr/bin/env python3

def cycle(move, amount, cap):
    result = move
    for _ in range(1, amount):
        result += 1
        if(move > cap):
            result = 0
    return result