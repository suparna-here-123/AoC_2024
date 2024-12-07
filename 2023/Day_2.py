
def getGameSets(file = r'2023/demo.txt') :
    f = open(file, 'r')
    lines = f.read().split('\n')
    final = []
    for game in lines :
        res = []
        sets = game.split(":")[1].split(";")
        for set_ in sets :
            set_RGB = [0] * 3
            num_colors = set_.strip().split(",")
            for x in num_colors :
                num, color = x.strip().split()
                if color == 'red' :
                    set_RGB[0] = int(num)
                elif color == 'green' :
                    set_RGB[1] = int(num)
                else :
                    set_RGB[2] = int(num)
            res.append(set_RGB)
        final.append(res)
    return final

ip = getGameSets()
print(ip)
res = 0
for gameNum, game in enumerate(ip, start=1) :
    print(game)
    valid = True
    for set_ in game :
        if not(set_[0] <= 12 and set_[1] <= 13 and set_[2] <= 14) :
            valid = False
            break
    
    if valid :
        res += gameNum

print(res)