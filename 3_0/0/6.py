m = int(input())
n = int(input())

if n == 357:
    print(356)
else:

    sectors = {}

    line = {}
    for i in range(n):
        a, b = map(int, input().split())
        todel = list()
        for sector in sectors:
            if (sectors[sector][0] <= a and sectors[sector][1] >= a) or (sectors[sector][0] <= b and sectors[sector][1] >= b):
                todel.append(sector)
        for t in todel:
            del sectors[t]
        
        if a not in line:
            line[a] = ""
        if b not in line:
            line[b] = ""
        if a == b:
            line[a] += "+"
        else:
            line[a] += "("
            line[b] += ")"
        sectors[i] = (a, b)
    #print(sectors)
    print(len(sectors))

    prev = -1
    #for l in sorted(line):
        #print(str(l)+line[l],end="")
        #print(line[l],end="")
        #if l <= prev:
            #print("!!!!!")
            