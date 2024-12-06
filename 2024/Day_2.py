#f = open("trial.txt", 'r')
f = open("Day_2_input.txt", 'r')

def calcFirstDiff(lst) :
    first, second = int(lst[0]), int(lst[1])
    return second - first

def validate(lst, removed) :
    global safe
    i = 1
    firstDiff = calcFirstDiff(lst)
    while i < len(lst) :
        prev, curr = int(lst[i - 1]), int(lst[i])
        currDiff = curr - prev
        
        if currDiff * firstDiff > 0 and (1 <= abs(currDiff) <= 3) :
            pass
            
        else :
            if removed :
                return False

            # see if removing any element helps ->
            for r in range(0, len(lst)) :
                woutThis = lst.copy()
                woutThis.pop(r)
                
                if validate(woutThis, True):
                    if r not in [i, i - 1] :
                        print(lst, " -> ", woutThis)
                    return True
            return False

        i += 1
    return True

safe = 0
for line in f.readlines() :
    lst = line.split()
    #print(lst, end = ' -> ')
    if validate(lst, False) :
        safe += 1
print(safe)
