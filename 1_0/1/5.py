s = input().split()
k1 = int(s[0])
m = int(s[1])
k2 = int(s[2])
p2 = int(s[3])
n2 = int(s[4])

if n2 > m:
    print("-1 -1")
else:
    resp = set()
    resn = set()
    p1 = -1
    n1 = -1
    p21 = p2 - 1
    k11 = k1 - 1
    i = 1
    if m != 1:
        for i in range(1000001):
            t = p21 * m * i + n2 * i
            if (k2 <= t and k2 > t - i):
                floorsbefore = k11 // i
                if len(resn) < 2:
                    floor = floorsbefore % m + 1
                    resn.add(floor)
                if len(resp) < 2:
                    entrance = floorsbefore // m + 1
                    resp.add(entrance)
    else:
        for i in range(1000001):
            t = p21 * i + n2 * i
            if (k2 <= t and k2 > t - i):
                floorsbefore = (k1 - 1) // i
                if len(resn) < 2:
                    floor = floorsbefore % 1 + 1
                    resn.add(floor)
                if len(resp) < 2:
                    entrance = floorsbefore // 1 + 1
                    resp.add(entrance)
           
           
    if len(resp) > 1:
        p1 = 0
    else:
        for r in resp:
            p1 = r
    if len(resn) > 1:
        n1 = 0
    else:
        for r in resn:
            n1 = r
    print(str(p1)+" "+str(n1))
