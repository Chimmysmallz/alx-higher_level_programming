#!/usr/bin/python3
"""
This file contains function that appends
a string at the end of a text file and
returns number of characters added
"""

def append_write(filename="", text=""):
    """returns the number of chars appended to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
