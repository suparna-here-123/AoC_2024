from collections import defaultdict

def processInput(file) :
    f = open(file, 'r')
    res = defaultdict(list)
    input = [] 
    inputBegins = False
    for line in f.readlines() :
        if not inputBegins :
            if line == '\n' :
                inputBegins = True
                continue
            before, after = [int(x) for x in line.strip().split("|")]
            res[before].append(after)

        else :
            input.append([int(x) for x in line.strip().split(",")])

    return res, input

#res, updates = processInput(r'Inputs\demo.txt')
res, updates = processInput(r'Inputs\Day_5_input.txt')

def puzzleOne() :
    # for i in res :
    #     print(i, "-> ", res[i])
    final = 0
    for update in updates :
        validUpdate, n = True, len(update)
        #print(f"Checking {update}")
        for i in range(n) :
            num = update[i]
            afterNum = update[i + 1 : ]
            allowed = res[num] if num in res else []
            if not all(x in allowed for x in afterNum) :
                validUpdate = False
                break
        
        # Finding median val if valid
        if validUpdate :
            final += update[n // 2]

    # Part 1
    print(final)

def puzzleTwo() :
    final = 0
    # for i in res :
    #     print(i, "-> ", res[i])
    for update in updates :
        foundInvalid = False
        n = len(update)
        i = 0
        while i < n :
            j = i + 1
            while j < n :
                while update[j] not in res[update[i]] :
                    foundInvalid = True                 # Invalid coz ele was not found in the allowed values
                    update[i], update[j] = update[j], update[i]
                j += 1
            i += 1
        
        if foundInvalid :
            final += update[n // 2]
    
    print(final)
        

print("Part 1")
puzzleOne()
print("Part 2")
puzzleTwo()