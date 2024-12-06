def processInput(file) :
    matrix = []
    f = open(file, 'r')
    for line in f.readlines() :
        matrix.append(line.strip())
    return matrix

#mat = processInput("Inputs/example_2.txt")
mat = processInput("Inputs/Day_4_input.txt")
count = 0

def checkColumn(word, lineIndex, charIndex) :
    column = ''.join(lineAndBelow[charIndex] for lineAndBelow in mat[lineIndex : ])
    #print(f"Column Checking {lineIndex} from {charIndex} = {column}")
    if column.startswith(word) :
        #print(f"{word} found in {line}")
        return True
    return False

def checkRow(word, line) :
    #print(f"Row Checking {line}")
    if line.startswith(word) :
        #print(f"{word} found in {line}")
        return True
    return False

# Checks and returns the indices of any next character in XMAS and SAMX - only X and S ge this function is called
def anyNext(word, row, col) :
    res = []
    diagEles = [(diagRow, diagCol) for diagRow in [row - 1, row + 1] for diagCol in [col - 1, col + 1]]
    #print(f"diagEles : {diagEles}")
    for i, j in diagEles :
        if (i == -1) or (j == -1) :
            continue
        try :
            #print("checking : ", mat[i][j])
            if mat[i][j] == word[1] :               # if word = XMAS, checks M, if word = SAMX, checks A
                res.append((i, j))
        except :
            #print(f'exception for {i, j}')
            continue
    return res

def checkDiagonal(row, col, pos, word, curIndex) : 
    if curIndex == len(word) - 1 :
        #print(f"{word} was found!")
        return True

    if pos == 'UL' :
        dRow, dCol = row - 1, col - 1
    elif pos == 'UR' :
        dRow, dCol = row - 1, col + 1
    elif pos == 'DL' :
        dRow, dCol = row + 1, col - 1
    else : 
        dRow, dCol = row + 1, col + 1
    
    try :
        if mat[dRow][dCol] == word[curIndex + 1] :
            #print(word[curIndex + 1], 'matched')
            #print(f"Checking {dRow}, {dCol}")
            return checkDiagonal(dRow, dCol, pos, word, curIndex + 1)
    except :
        return False
    return False

for lineIndex in range(len(mat)) :
    line = mat[lineIndex]
    for i in range(len(line)) :
        char = line[i]
        # Horizontal + Vertical - Forward and Backwards
        if char == 'X' :
            print(f"Line {lineIndex}, char {i}")

            if checkRow("XMAS", line[i : ]) :
                print("Row has")
                count += 1
            if checkColumn("XMAS", lineIndex, i) :
                print("Column has")
                count += 1
            possibleNext = anyNext('XMAS', lineIndex, i)
            #print(f"Possible diagonals at {possibleNext}")
            for MPos in possibleNext :
                mRow, mCol = MPos
                if mRow < lineIndex and mCol < i :          # Upper left diagonal
                    pos = 'UL'
                elif mRow < lineIndex and mCol > i :        # Upper right diagonal
                    pos = 'UR'
                elif mRow > lineIndex and mCol < i :        # Down Left diagonal
                    pos = 'DL'
                else :                                      # Down right diagonal
                    pos = 'DR'
                if checkDiagonal(mRow, mCol, pos, 'MAS', 0) :
                    print(f"Diagonal has\n")
                    count += 1

        # Not checking diagonals from S coz of repetition        
        elif char == 'S' :
            print(f"Line {lineIndex}, char {i}")
            if checkRow("SAMX", line[i : ]) :
                print("Row has")
                count += 1
            if checkColumn("SAMX", lineIndex, i) :
                print("Column has")
                count += 1
print(count)