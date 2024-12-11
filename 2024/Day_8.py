from collections import defaultdict
def parse(file) :
    res = []
    f = open(file, 'r')
    for line in f.readlines() :
        line = line.strip()
        line = [char for char in line]
        res.append(line)
    return res

def find(grid) :
    freq = defaultdict(list)
    seen = set()
    m, n = len(grid), len(grid[0])
    res = 0
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
                                    res += 1
                                    seen.add((X, Y))
                                # grid[X][Y] != '#':
                                #     res += 1
                                #     if grid[X][Y] == '.' :
                                #         grid[X][Y] = '#'
                                #     printGrid(grid)

                freq[c].append((row, col))
    with open('day_8_op.txt', 'w') as f:
        for l in grid :
            f.write(''.join(l) + "\n")
    print(f"freq : {freq.keys()}")
    print(f"res : {res}")
    printGrid(grid)

    return res



def printGrid(grid) :
    nums = list(range(0, len(grid[0]), 1))
    print("   ", end = '')
    for num in nums :
        print(num, end = '    ')
    print()
    for i, line in enumerate(grid) :
        print(i, line)

def main() :
    grid = parse(r"C:\Users\HP\OneDrive\Desktop\AdventOfCode\2024\Inputs\demo.txt")
    #grid = parse(r"C:\Users\HP\OneDrive\Desktop\AdventOfCode\2024\Inputs\Day_8_input.txt")
    #printGrid(grid)
    print(find(grid))


if __name__== "__main__" :
    main()