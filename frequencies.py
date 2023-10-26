"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {} #dictionary with (key, value pairs)
    x = 0
    keys = []
    for x in items:
        frequencies.update({str(x):0})
        valueSum = 0
        for y in items:
            if (y == x):
                valueSum += 1
        frequencies.update({str(x):valueSum})
    return frequencies

dictionary = frequencies([1,2,2,2,3,3,4,4,4,6,6,6,66,6])
print(dictionary)
