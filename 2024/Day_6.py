import sys
from collections import defaultdict

file = r'Inputs\demo.txt' if sys.argv[1] == '1' else r'Inputs\Day_6_input.txt'
#file = r'2024\Inputs\demo.txt'
f = open(file, 'r')

lines = []
for line in f.readlines() :
    chars = []
    for char in line.strip() :
        chars.append(char)
    lines.append(chars)

def findStart() :
    for lineIndex, line in enumerate(lines) :
        for charIndex, char in enumerate(line) :
            if char == '^' :
                return (lineIndex, charIndex)
            
def markX(lineInd, colInd) :
    global part_1
    if lines[lineInd][colInd] != 'X' :
        lines[lineInd][colInd] = 'X'
        part_1 += 1

    # for line in lines :
    #     print(line)
    # print()

part_1 = 0
curRow, curCol = findStart()
m, n = len(lines), len(lines[0])
dir = 'U'
stop = False

corners = set()            # [(row, col)] of corners
part_2 = 0

def obstacleHere(row, col) :
    global part_2
    found = False
    inRow = [(r, c) for r,c in corners if r == row]
    inCol = [(r, c) for r,c in corners if c == col]
    for rowPt in inRow :
        for colPt in inCol :
            potentialDiag = (colPt[0], rowPt[1])
            if lines[colPt[0]][rowPt[1]] == 'X' :
                part_2 += 1
                #corners.add((colPt[0], rowPt[1]))            # Adding the new corner that completed a rectangle
                found = True
                break
        if found :
            break
        

def intersecting(row, col) :
    if lines[curRow][curCol] == 'X' :
        corners.add((curRow, curCol))

while not stop :
    while dir == 'U' :
        obstacleHere(curRow, curCol)
        #intersecting(curRow, curCol)
        markX(curRow, curCol)

        if curRow > 0 :
            if lines[curRow - 1][curCol] != '#' :
                curRow -= 1
            else :      # turn right
                corners.add((curRow, curCol))
                curCol += 1
                dir = 'R'
                break
        else :
            stop = True
            break

    
    while dir == 'D' :
        obstacleHere(curRow, curCol)
        #intersecting(curRow, curCol)
        markX(curRow, curCol)
        if curRow < m-1 :
            if lines[curRow + 1][curCol] != '#' :
                curRow += 1
            else :      # turn right
                corners.add((curRow, curCol))
                curCol -= 1
                dir = 'L'
                break
        else :
            stop = True
            break
    
    while dir == 'L':
        obstacleHere(curRow, curCol)
        #intersecting(curRow, curCol)
        markX(curRow, curCol)
        if curCol > 0 :
            if lines[curRow][curCol - 1] != '#' :
                curCol -= 1
            else :      # turn right
                corners.add((curRow, curCol))
                curRow -= 1
                dir = 'U'
                break
        else :
            stop = True
            break
    
    while dir == 'R' :
        obstacleHere(curRow, curCol)
        #intersecting(curRow, curCol)
        markX(curRow, curCol)
        if curCol < n - 1 :
            if lines[curRow][curCol + 1] != '#' :
                curCol += 1
            else :      # turn right
                corners.add((curRow, curCol))
                curRow += 1
                dir = 'D' 
                break
        else :
            stop = True
            break
        
#print(part_1)
print(part_2)