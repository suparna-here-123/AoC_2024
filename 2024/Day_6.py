import sys
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
    global count
    if lines[lineInd][colInd] != 'X' :
        lines[lineInd][colInd] = 'X'
        count += 1

    # for line in lines :
    #     print(line)
    # print()

count = 0
curRow, curCol = findStart()
m, n = len(lines), len(lines[0])
dir = 'U'

stop = False
while not stop :
    # Mark X for position I'm currently in
    while dir == 'U' :
        markX(curRow, curCol)
        if curRow > 0 :
            if lines[curRow - 1][curCol] != '#' :
                curRow -= 1
            else :      # turn right
                curCol += 1
                dir = 'R'
                break
        else :
            stop = True
            break

    
    while dir == 'D' :
        markX(curRow, curCol)
        if curRow < m-1 :
            if lines[curRow + 1][curCol] != '#' :
                curRow += 1
            else :      # turn right
                curCol -= 1
                dir = 'L'
                break
        else :
            stop = True
            break
    
    while dir == 'L':
        markX(curRow, curCol)
        if curCol > 0 :
            if lines[curRow][curCol - 1] != '#' :
                curCol -= 1
            else :      # turn right
                curRow -= 1
                dir = 'U'
                break
        else :
            stop = True
            break
    
    while dir == 'R' :
        markX(curRow, curCol)
        if curCol < n - 1 :
            if lines[curRow][curCol + 1] != '#' :
                curCol += 1
            else :      # turn right
                curRow += 1
                dir = 'D' 
                break
        else :
            stop = True
            break
        
print(count)