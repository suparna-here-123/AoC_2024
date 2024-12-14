def find(row, col, num, seen) :
    global m, n, grid
    if 0 <= row < m and 0 <= col < n :
        if int(grid[row][col]) == num :
            if num == 9 :
                seen.add((row, col))
            
            else :
                find(row-1, col, num+1, seen)
                find(row+1, col, num+1, seen)
                find(row, col-1, num+1, seen)
                find(row, col+1, num+1, seen)

def parseFile() :
    f = open(r"Inputs\Day_10.txt", 'r')
    grid = []
    for line in f.readlines() :
        line = line.strip()
        grid.append([x for x in line])
    return grid

grid = parseFile()
m, n = len(grid), len(grid[0])
final = 0
for lineInd, line in enumerate(grid) :
    for charInd, char in enumerate(line) :
        if char == '0' :
            seen = set()
            find(lineInd, charInd, 0, seen)
            print(f"From trailhead at {lineInd}, {charInd} -> {seen}")
            final += len(seen)

print(final)