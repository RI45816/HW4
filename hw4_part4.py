# File: hw4_part4.py
# Author: Uzoma Uwanamodo
# Date: 10/5/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Continously prompt user until they enter a username of the required length and character content
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    height = int(input("Please enter the starting height of the hailstone: ")) # Prompt the user for the starting height of the hailstone
    STOP_HEIGHT = 1 # The height the hailstone stops at
    FALLING_DIVIDER = 2 # What to divide the current height at to simulate a falling hailstone
    BOUNCE_MULTIPLIER = 3 # What to multiply the hailstone height by if the current height is odd
    BOUNCE_CONSTANT = 1 # What to add to the hailstone height after multliplying it by the BOUNCE_CONSTANT
    while True:
        height = height // FALLING_DIVIDER if not height % 2 else height * BOUNCE_MULTIPLIER + BOUNCE_CONSTANT
        if height != STOP_HEIGHT:
            print("Hail is currently at height %s" % height)
        else:
            break
    print("Hail stopped at height %s" % STOP_HEIGHT)


main()