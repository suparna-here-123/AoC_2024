import re

def processInput(file) :
    matrix = []
    f = open(r'2024/' + file, 'r')
    for line in f.readlines() :
        matrix.append('ZZZ' + line.strip() + 'ZZZ')

    # Adding padding
    matrix.insert(0, 'Z' * len(matrix[0]))
    matrix.append('Z' * len(matrix[0]))

    return matrix

#mat = processInput("Inputs/demo.txt")
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
        if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[dRow][dCol] == word[curIndex + 1] :
            #print(word[curIndex + 1], 'matched')
            #print(f"Checking {dRow}, {dCol}")
            return checkDiagonal(dRow, dCol, pos, word, curIndex + 1)
    except :
        return False
    return False

# Part 2
for lineIndex in range(1, len(mat)) :
    line = mat[lineIndex]
    for i in range(3, len(line) - 3) :
        threeChars = line[i : i + 3]
        if (re.match('M.S', threeChars) and checkDiagonal(lineIndex, i, 'DR', 'MAS', 0) and checkDiagonal(lineIndex, i + 2, 'DL', 'SAM', 0)) or \
           (re.match('S.M', threeChars) and checkDiagonal(lineIndex, i, 'DR', 'SAM', 0) and checkDiagonal(lineIndex, i + 2, 'DL', 'MAS', 0)) or \
           (re.match('M.M', threeChars) and checkDiagonal(lineIndex, i, 'DR', 'MAS', 0) and checkDiagonal(lineIndex, i + 2, 'DL', 'MAS', 0)) or \
           (re.match('S.S', threeChars) and checkDiagonal(lineIndex, i, 'DR', 'SAM', 0) and checkDiagonal(lineIndex, i + 2, 'DL', 'SAM', 0)) :
                count += 1
    
print(count)


# Part 1
# for lineIndex in range(1, len(mat)) :
#     line = mat[lineIndex]
#     for i in range(3, len(line) - 3) :
#         char = line[i]
#         # Horizontal + Vertical - Forward and Backwards
#         if char == 'X' :
#             #print(f"Line {lineIndex}, char {i}")

#             if checkRow("XMAS", line[i : ]) :
#                 #print("Row has")
#                 count += 1
#             if checkColumn("XMAS", lineIndex, i) :
#                 #print("Column has")
#                 count += 1
#             possibleNext = anyNext('XMAS', lineIndex, i)
#             #print(f"Possible diagonals at {possibleNext}")
#             for MPos in possibleNext :
#                 mRow, mCol = MPos
#                 if mRow < lineIndex and mCol < i :          # Upper left diagonal
#                     pos = 'UL'
#                 elif mRow < lineIndex and mCol > i :        # Upper right diagonal
#                     pos = 'UR'
#                 elif mRow > lineIndex and mCol < i :        # Down Left diagonal
#                     pos = 'DL'
#                 else :                                      # Down right diagonal
#                     pos = 'DR'
#                 if checkDiagonal(mRow, mCol, pos, 'MAS', 0) :
#                     #print(f"Diagonal has\n")
#                     count += 1

#         # Not checking diagonals from S coz of repetition        
#         elif char == 'S' :
#             #print(f"Line {lineIndex}, char {i}")
#             if checkRow("SAMX", line[i : ]) :
#                 #print("Row has")
#                 count += 1
#             if checkColumn("SAMX", lineIndex, i) :
#                 #print("Column has")
#                 count += 1
# print(count)