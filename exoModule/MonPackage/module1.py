# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:01:30 2019

@author: miguel
"""

def dire_bonjour():
    print("Hello world")
    
def multiplier(a,b):
    """
    Multiplie a par b
    
    :Exemple:
    >>> multiplier(4,4)
    17
    """
    return a+b


# print(__name__)

if __name__ == "__main__":
    # print("Programme test")
    import doctest
    doctest.testmod()