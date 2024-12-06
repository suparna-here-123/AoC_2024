import re
f = open("Inputs/Day_3_input.txt", 'r')
#s = f.read()
s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def puzzleOne() :
    lst = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", s)
    res = 0
    for exp in lst :
        args = exp[4 : -1].split(",")
        res += int(args[0]) * int(args[1])
    print(res)

def mul(x, y) :
    return x * y

def puzzleTwo() :
    global s
    res, ignore = 0, False
    lst = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", s)
    print(lst)
    for exp in lst :
        if exp == "don't()" :
            ignore = True
        elif exp == "do()" :
            ignore = False
        else :
            if not ignore :
                res += eval(exp)
    print(res)

if __name__ == "__main__" :
    puzzleTwo()
