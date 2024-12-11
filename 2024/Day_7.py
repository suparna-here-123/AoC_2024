from pathlib import Path
from copy import copy
import sys

def parse(file = Path(r'2024\Inputs\demo.txt')):
    s = file.read_text().split("\n")
    allCalib = []
    for line in s :
        calib, args = line.strip().split(":")
        args = args.strip().split()
        allCalib.append([calib, args])
    return allCalib

def opCombos(s, maxLen) :
    if len(s) == maxLen :
        return [s]

    withPlus = opCombos(s + '+', maxLen)
    withMul = opCombos(s + '*', maxLen)
    withConcat = opCombos(s + '|', maxLen)
    return withPlus + withMul + withConcat

def partOne(allCalib) :
    res = []
    for X in allCalib :
        #print(f"for {X}")
        calib, args = X
        allCombos = opCombos('', len(args) - 1)
        for combo in allCombos :
            #print(f"Checking combo : {combo}")
            argsCopy = copy(args)
            cSum = int(argsCopy[0])

            # MAKE THIS SIMPLER
            for i, char in zip(range(1, len(args) + len(combo), 2), combo) :
                argsCopy.insert(i, char)
                rightArg = int(argsCopy[i + 1])
                cSum = cSum + rightArg if char == '+' else cSum * rightArg

            #exp = ''.join(argsCopy)
            #if eval(exp) == int(calib) :
            if cSum == int(calib) :
                res.append(int(calib))
                break
    return sum(res)

def partTwo(allCalib) :
    res = []
    for X in allCalib :
        print(f"for {X}")
        calib, args = X
        allCombos = opCombos('', len(args) - 1)
        
        for combo in allCombos :
            #print(f"Checking combo : {combo}")
            argsCopy = copy(args)
            cSum = int(argsCopy[0])

            # MAKE THIS SIMPLER
            for i, char in zip(range(1, len(args) + len(combo), 2), combo) :
                argsCopy.insert(i, char)
                rightArg = int(argsCopy[i + 1])

                if char == '+' :
                    cSum += rightArg
                elif char == '*' :
                    cSum *= rightArg
                else :
                    cSum = int(str(cSum) + str(rightArg))

            if cSum == int(calib) :
                res.append(int(calib))
                break

    return sum(res)

def main() :
    filePath = Path(sys.argv[1])
    allCalib = parse(filePath)
    #allCalib = parse()
    #print(partOne(allCalib))
    print(partTwo(allCalib))

if __name__ == '__main__' :
    main()