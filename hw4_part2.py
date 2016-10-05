# File: hw4_part2.py
# Author: Uzoma Uwanamodo
# Date: 10/5/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description:
# Find the result of modulus division between two numbers
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():
    firstNumber = int(input("Please enter the first  number: ")) # Prompt the user for the first number
    secondNumber = int(input("Please enter the second number: ")) # Prompt the user for the second number
    print("%s %% %s = %s" % (firstNumber, secondNumber, (firstNumber - (firstNumber // secondNumber) * secondNumber)))
main()