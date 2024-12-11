from collections import defaultdict
def parse(file) :
    res = []
    f = open(file, 'r')
    for line in f.readlines() :
        line = line.strip()
        line = [char for char in line]
        res.append(line)
    return res

def findOne(grid) :
    freq = defaultdict(list)
    seen = set()
    m, n = len(grid), len(grid[0])
    #res = 0
    for row in range(m) :
        for col in range(n) :
            c = grid[row][col] 
            if c not in ['#', '.']:
                neighbors = freq[c]
                for nb in neighbors :
                    rowD, colD = nb[0] - row, nb[1] - col
                    for A in ((row, col), nb) :
                        for mul in (-1, 1) :
                            X, Y = A[0] + (mul * rowD), A[1] + (mul * colD)
                            if (X, Y) not in ((row, col), nb) and \
                                0 <= X < m and 0 <= Y < n and (X, Y) not in seen:
                                    #res += 1
                                    seen.add((X, Y))
                freq[c].append((row, col))
    #return res
    return len(seen)

def findTwo(grid) :
    freq = defaultdict(list)
    seen = set()
    m, n = len(grid), len(grid[0])
    for row in range(m) :
        for col in range(n) :
            c = grid[row][col]
            if c not in ['#', '.']:
                neighbors = freq[c]
                for nb in neighbors :
                    rowD, colD = nb[0] - row, nb[1] - col
                    for mul in (-1, 1) :
                        X, Y = row + (mul * rowD), col + (mul * colD)
                        while 0 <= X < m and 0 <= Y < n :
                                seen.add((X, Y))
                                seen.add((row, col))
                                seen.add(nb)
                                if grid[X][Y] == '.' :
                                    grid[X][Y] = '#'
                                
                                X, Y = X + (mul * rowD), Y + (mul * colD)
                freq[c].append((row, col))
    return len(seen)

def printGrid(grid) :
    nums = list(range(0, len(grid[0]), 1))
    print("   ", end = '')
    for num in nums :
        print(num, end = '    ')
    print()
    for i, line in enumerate(grid) :
        print(i, line)

def main() :
    #grid = parse(r"Inputs\demo.txt")
    grid = parse(r"Inputs\Day_8_input.txt")
    print(findTwo(grid))


if __name__== "__main__" :
    main()