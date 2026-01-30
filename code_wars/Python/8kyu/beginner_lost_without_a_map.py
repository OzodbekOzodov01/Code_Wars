# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    doubled = []
    for n in a:
        doubled.append(n*2)
    return doubled