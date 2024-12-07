'''
Edge Case -> Overlapping words like twone -> 2 and 1
Approach -> consider every character in the line and check if its starts with a word
Or use regex external library for overlapping search

'''

import re
from pathlib import Path

def parse(filePath) :
    f = open(filePath, 'r')
    return f.readlines()

def puzzleOne(puzzleInput) :
    res = 0
    for line in puzzleInput :
        first = int(re.search(r"\d", line).group())
        last = int(re.search(r"\d", line[-1::-1]).group())
        res += (10 * first) + last
    return res

def puzzleTwo(puzzleInput) :
    res = 0
    first, last = None, None
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in puzzleInput :
        digits = []
        for i, c in enumerate(line) :
            if c.isdigit() :
                digits.append(int(c))
            else :
                if c in 'otfsen' :
                    for val, word in enumerate(words, start=1):
                        if line[i : ].startswith(word) :
                            digits.append(val)
                            break
        res += (10 * digits[0]) + digits[-1]
    return res


input = parse("Day_1_input.txt")
#input = parse("example.txt")
# print(puzzleOne(input))
print(puzzleTwo(input))
