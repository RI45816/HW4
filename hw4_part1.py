# File: hw4_part1.py
# Author: Uzoma Uwanamodo
# Date: 10/5/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Continously prompt user until they enter a username of the required length
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    while True:
        username = input("Please enter your username: ").strip() # Ask user to input a username
        MINIMUM_CHARACTERS = 4 # Minimum amount of characters allowed in a username
        MAXIMUM_CHARACTERS = 12 # Maximum amount of characters allowed in a username
        if not len(username) in range(MINIMUM_CHARACTERS,MAXIMUM_CHARACTERS+1): # The username is not the correct length
            print("That username is too %s.\nThe username must be between %s and %s characters." % (("short" if len(username) < MINIMUM_CHARACTERS else "long"),MINIMUM_CHARACTERS,MAXIMUM_CHARACTERS)) # Inform the user
        else:
            print("Thank you for choosing the username %s" % username) # Let the user know they were successful
            break
            
main()
