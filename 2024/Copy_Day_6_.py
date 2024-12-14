import sys
from collections import defaultdict

#file = r'Inputs\demo.txt' if sys.argv[1] == '1' else r'Inputs\Day_6_input.txt'
file = r'2024\Inputs\demo.txt'
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
            
startRow, startCol = findStart()
dir = 0                         # Facing up
seen = set()                    # (row, col, dir)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]          # U, R, D, L
m, n = len(lines) - 1, len(lines[0]) - 1
part1 = 0
part2 = 0

def myPrint() :
    for line in lines :
        print(line)

def partOne() :
    global seen, dir, m, n
    stop = False
    curRow, curCol = startRow, startCol
    while not stop :
        seen.add((curRow, curCol))
        #myPrint()

        nextRow = curRow + dirs[dir][0]
        nextCol = curCol + dirs[dir][1]

        if (0 <= nextRow <= m) and (0 <= nextCol <= n) :
            if lines[nextRow][nextCol] == '#' :
                dir = (dir + 1) % 4
                curRow = curRow + dirs[dir][0]
                curCol = curCol + dirs[dir][1]
            else :
                curRow, curCol = nextRow, nextCol
        
        else :
            stop = True

def willLoop(oi, oj, lines) :
    global dirs, m, n
    grid = lines

    if grid[oi][oj] == '#' :
        return False
    
    grid[oi][oj] = '#'
    seen = set()
    curRow, curCol, dir = startRow, startCol, 0
    while True :
        if (curRow, curCol, dir) in seen :
            return True
        
        # Point hasn't been seen -> add it and move to next point in that direction
        seen.add((curRow, curCol, dir))
        
        nextRow = curRow + dirs[dir][0]
        nextCol = curCol + dirs[dir][1]

        if (0 <= nextRow <= m) and (0 <= nextCol <= n) :
            if grid[nextRow][nextCol] == '#' :
                dir = (dir + 1) % 4
            else :
                curRow, curCol = nextRow, nextCol
            
        else :
            return False

partOne()
for pos in seen :
    if pos != (startRow, startCol) :
        part2 += willLoop(pos[0], pos[1], lines)
print(part2)