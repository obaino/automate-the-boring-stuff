#!/usr/bin/env python3
# my solution ver. 2

import random
from codetiming  import Timer


streakNo = 6
flips = 100
numberOfStreaks = 0

def main():
    t = Timer()
    runs = int(input("How many times to run the experiment? "))
    # flips_per_run = int(input("How many times to flip the coin per run? "))
    # print(head_tails_list(flips_per_run))

    t.start()
    for experimentNumber in range(runs):
        print(f"{check_for_streak(head_tails_list(flips)) / 100}%")
    t.stop()

def head_tails_list(flips):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipsList = []
    for i in range(flips):
        flipsList.append(random.randint(0, 1))
    return flipsList

def check_for_streak(lst):
    # Code that checks if there is a streak of 6 heads or tails in a row.
    global numberOfStreaks
    n = 0 #index in lst
    # run the check for a length of six elements until the end of the list
    while n+streakNo < len(lst) - streakNo:
        sumvalue=0                  # 
        for i in range(streakNo):
            sumvalue += lst[n+i]
        if sumvalue == streakNo or sumvalue == 0:
            numberOfStreaks += 1
        n += 1
    return numberOfStreaks


if __name__ == "__main__":
    main()
