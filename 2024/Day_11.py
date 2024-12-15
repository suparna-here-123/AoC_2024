from collections import defaultdict
from functools import cache
import timeit

# def split(lst : list) :               -> Part 1
#     if len(lst) == 1 :
#         return applyRule(lst[0])

#     left = split(lst[0 : len(lst)//2])
#     right = split(lst[len(lst)//2 : ])
#     return left + right

def applyRule(s : str) :
    global splitMap 
    if s in splitMap :                          # Using saved value
        return splitMap[s]
    
    if s == '0' :
        splitMap['0'] = ['1']
    
    elif len(s) % 2 == 0 :
        left, right = s[0 : len(s)//2], s[len(s)//2 : ]
        splitMap[s] = [str(int(left)), str(int(right))]

    else :
        splitMap[s] = [str(2024 * int(s))]

    return splitMap[s]

ip = '2 72 8949 0 981038 86311 246 7636740'
#ip = '125 17'
stones = [int(x) for x in ip.split()]

@cache                                                                  # 40% faster if you cache this also lol
def anotherRule(stone : int) :
    if stone == 0 :
        return 1
    
    # If stone is even-length string
    s = str(stone)
    if len(s) % 2 == 0 :
        return (int(s[:len(s)//2]), int(s[len(s)//2 :]))
    
    # If neither of above rules
    return stone * 2024
    
@cache
def count(stone, stepsRem) :
    if stepsRem == 0 :              # No blinks remaining, just return the stone
        return 1
    
    if stone == 0 :
        return count(anotherRule(stone), stepsRem - 1)

    # If stone is even-length string
    s = str(stone)
    if len(s) % 2 == 0 :
        l, r = anotherRule(stone)
        return count(l, stepsRem - 1) + count(r, stepsRem - 1)
    
    # If neither of above rules
    return count(anotherRule(stone), stepsRem - 1)

# Your function call inside a lambda or function wrapper
execution_time = timeit.timeit(lambda: sum(count(stone, 75) for stone in stones), number=1)

print(f"Execution time: {execution_time:.4f} seconds")