#!/usr/bin/python3
"""This module reads a file name"""


def read_file(filename=""):
    """Function that Prints the contents of a file
    
    Args:
     filename: name of the file
     
    Raises:
        Exception: when file can't be opened
        
    """
    
    with open(filename) as file:
        read = file.read()
        print(read, end='')
