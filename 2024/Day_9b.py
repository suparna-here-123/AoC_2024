'''
1) Attempt to move files in decreasing order from the last
2) EVERY FILE ONLY ONCE

'''

from collections import OrderedDict, defaultdict
#diskMap = '12345'
#diskMap = '2333133121414131402'
diskMap = open(r"C:\Users\HP\OneDrive\Desktop\AdventOfCode\2024\Inputs\Day_9_input.txt", 'r').read()


disk = []

# Finds fileIDs, their current position, their sizes + positions of free spaces and their sizes
def find() :
    global diskMap
    fileIDSizeMap = {}
    freePosSizeMap = OrderedDict()
    
    fileID = 0
    freePos = 0
    curPos = 0
    file_or_free = 1            # File : 1, Free : 0
    for numBlocks in diskMap :
        numBlocks = int(numBlocks)
        if file_or_free == 1 :
            fileIDSizeMap[fileID] = [curPos, numBlocks]
            fileID += 1
            file_or_free = 0 
        
        else :
            freePosSizeMap[curPos] = numBlocks
            file_or_free = 1
        curPos += numBlocks

    return (dict(sorted(fileIDSizeMap.items(), key = lambda item : item[0], reverse=True)), freePosSizeMap)

def checksum(fileMap) :
    res = 0
    for fileID, fileInfo in fileMap.items() :
        startPos, fileSize = fileInfo
        for pos in range(startPos, startPos + fileSize) :
            res += fileID * pos
    return res

def partTwo(fileIDSizeMap, freePosSizeMap) :
    freeLst = list(freePosSizeMap.items())
    
    for i, fileInfo in enumerate(fileIDSizeMap.items()) :            # for every file ID in descending order
        fileID, filePos, fileSize = fileInfo[0], fileInfo[1][0], fileInfo[1][1]
        for j, freeInfo in enumerate(freeLst) :                            # check all possible free spaces...
            freePos, freeSize = freeInfo
            if freePos < filePos :                                                  # ...that are occur before this file's blocks
                if freeSize >= fileSize :
                    freeLst[j] = (freePos + fileSize, freeSize - fileSize)
                    fileIDSizeMap[fileID][0] = freePos
                    break                
            
            # Stop checking free spaces beyond current file position
            else :
                break
    return fileIDSizeMap

fileIDSizeMap, freePosSizeMap = find()
# print(fileIDSizeMap)
# print()
# print(freePosSizeMap)
fileOut = partTwo(fileIDSizeMap, freePosSizeMap)
#print(fileOut)
print(f"Checksum : {checksum(fileOut)}")
# print(fileIDSizeMap)
# print()
# print(freePosSizeMap)