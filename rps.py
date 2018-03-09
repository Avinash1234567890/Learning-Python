#!/usr/bin/env python3
import sqlite3 as sql
from random import randint
from translate import str_to_num
from proc import calc_freq, arb

move_list = [0, 1, 2]
connection = sql.connect(":memory:") # HACK: Use a database file to keep permanent changes
db = connection.cursor()
db.execute("DROP TABLE IF EXISTS rps") # DEBUG
db.execute("CREATE TABLE rps (move)")
for val in move_list:
    db.execute("INSERT INTO rps VALUES (?)", (val,))
    connection.commit()
# HACK: To get all, use SQL select, then db.fetch___

def add_move(move):
    move_list.append(int(move))
    db.execute("INSERT INTO rps VALUES (?)", (move,))
    connection.commit()
    db.execute("SELECT * FROM rps")
    print(db.fetchall())

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

print("Enter a move for the prompt. Enter 'stop' to stop.")
while(42):
    move = input("Enter move(rock,paper,or scissors) :: ")
    if(move == "stop"):
        print("Ending program...")
        break

    move = str_to_num(move)

    add_move(move)

    choice = spin(calc_freq(move_list))
    result = arb(move,choice)
connection.close()