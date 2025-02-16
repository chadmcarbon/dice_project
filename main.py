#!/usr/bin/env python3
"""
This program imports the Die Class from the die.py module, creates an instance 
of the die, and calls the method that prints the rolled numbers.
"""
from die.die import Die, TenSideDie

def main():

    #  Create an instance of the Die Class and call roll die method
    my_die = Die()
    my_die.roll_die()

    # Create instance of the TenSided Die Class and call overridden method
    my_new_die = TenSideDie()
    my_new_die.roll_die()

if __name__ == '__main__':
    main()