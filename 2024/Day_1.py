from collections import Counter
f = open('Day_1_input.txt', 'r')
l1, l2 = [], []

def merge(A, B) :
    res = []
    a, b = 0, 0
    while a < len(A) and b < len(B) :
        if A[a] < B[b] :
            res.append(A[a])
            a += 1
        elif A[a] > B[b] :
            res.append(B[b])
            b += 1
        else :
            res.extend([A[a], B[b]])
            a += 1
            b += 1
    
    while a < len(A) :
        res.append(A[a])
        a += 1
    
    while b < len(B) :
        res.append(B[b])
        b += 1
    
    return res

def mergeSort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = len(arr) // 2
    left, right = arr[0 : mid], arr[mid : ]
    leftSorted = mergeSort(left)
    rightSorted = mergeSort(right)
    return merge(leftSorted, rightSorted)

def read() :
    for line in f.readlines() :
        x, y = line.split("   ")
        l1.append(int(x))
        l2.append(int(y))
    return l1, l2

def puzzle_one(l1, l2) :
    diff = 0
    for i in range(len(l1)) :
        diff += abs(l1[i] - l2[i])
    return diff

def puzzle_two(l1, l2) :
    sim_score = 0
    counts = Counter(l2)
    for num in l1 :
        sim_score += num * counts[num]
    return sim_score




def main() :
    l1, l2 = read()
    #l1, l2 = mergeSort(l1), mergeSort(l2)
    #print(f"Puzzle one : {puzzle_one(l1, l2)}")
    # l1 = [3,4,2,1,3,3]
    # l2 = [4,3,5,3,9,3]
    print(f"Puzzle two : {puzzle_two(l1, l2)}")


if __name__ == "__main__" :
    main()