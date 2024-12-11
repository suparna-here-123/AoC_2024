#diskMap = '12345'
#diskMap = '2333133121414131402'
diskMap = open(r"C:\Users\HP\OneDrive\Desktop\AdventOfCode\2024\Inputs\demo.txt", 'r').read()
fileID = 0
file_or_free = 1            # File : 1, Free : 0

disk = []

for numBlocks in diskMap :
    numBlocks = int(numBlocks)
    if file_or_free == 1 :
        disk.extend([str(fileID)] * numBlocks)
        fileID += 1
        file_or_free = 0
    
    else :
        disk.extend('.' * numBlocks)
        file_or_free = 1

#print(''.join(disk))

# Placing left pointer at first free space
left, right = 0, len(disk) - 1

while left < right :
    while disk[left] != '.' and left < len(disk):
        left += 1
    
    while disk[right] == '.' and right >= 0:
        right -= 1

    # swap free block w file block
    if left < right :
        disk[left], disk[right] = disk[right], disk[left]
        left += 1
        right -= 1

print(''.join(disk))

res = 0
for blockPos, fileID in enumerate(disk) :
    if fileID != '.' :
        res += blockPos * int(fileID)
    else :
        break
print(res)