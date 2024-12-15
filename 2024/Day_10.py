def partOne(row, col, num, seen) :
    global m, n, grid
    if 0 <= row < m and 0 <= col < n :
        if grid[row][col] == str(num) :
            #grid[row][col] = 'X'
            print(f"{num} at {row}, {col}")
            if num == 9 :
                #seen.add((row, col))
                seen.append((row, col))
                print(f"{num} at {row}, {col}")
                print()
            
            else :
                partOne(row-1, col, num+1, seen)
                partOne(row+1, col, num+1, seen)
                partOne(row, col-1, num+1, seen)
                partOne(row, col+1, num+1, seen)

def parseFile() :
    f = open(r'C:\Users\HP\OneDrive\Desktop\AdventOfCode\2024\Inputs\Day_10_input.txt', 'r')
    grid = []
    for line in f.readlines() :
        line = line.strip()
        grid.append([x for x in line])
    return grid

grid = parseFile()
for line in grid :
    print(line)

m, n = len(grid), len(grid[0])
final = 0
for lineInd, line in enumerate(grid) :
    for charInd, char in enumerate(line) :
        if char == '0' :
            count = 0
            # seen = set()
            lst = []
            partOne(lineInd, charInd, 0, lst)
            print(f"From trailhead at {lineInd}, {charInd} -> {lst}")
            final += len(lst)

print(final)