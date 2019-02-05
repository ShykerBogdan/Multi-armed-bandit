from time import perf_counter
from config import c, m, seed


def rand(a, b):
    """
    Generates random number on the interbal [a,b]
    Returns float 
    """
    global seed
    i_next = c*seed % m
    seed = i_next
    return round((i_next/m)*(b-a) + a,5)


def randInt(a, b):
    """
    Generates random int number on the interbal [a,b]
    Returns integer 
    """
    return round(rand(a, b))


def randSequence(n, a, b):
    """
    Generates random sequence on the interbal [a,b]
    n: count of nums to generate
    Returns list 
    """
    global seed
    randlist = []
    for i in range(n):
        i_next = c*seed % m
        seed = i_next
        randlist.append(((i_next/m)*(b-a) + a))
    return randlist


def randIntSequence(n, a, b):
    """
    Generates random sequence of integers on interval [a,b]
    n: count of nums to generate    
    Retruns list
    """
    return [round(num) for num in randSequence(n, a, b)]
