s = input().split()

if len(s) < 3:
    if int(s[0]) <= int(s[1]):
        print(' '.join(s))
    else:
        print(' '.join(reversed(s)))
else:
    minusmin1 = 0
    minusmin2 = 0
    plusmax1 = 0
    plusmax2 = 0
    for i in s:
        ii = int(i)
        if ii < 0:
            if ii <= minusmin1:
                minusmin2 = minusmin1
                minusmin1 = ii
            elif ii <= minusmin2:
                minusmin2 = ii
        if ii > 0:
            if ii >= plusmax1:
                plusmax2 = plusmax1
                plusmax1 = ii
            elif ii >= plusmax2:
                plusmax2 = ii
    if minusmin1*minusmin2 > plusmax1*plusmax2:
        print(str(minusmin1)+" "+str(minusmin2))
    else:
        print(str(plusmax2)+" "+str(plusmax1))
        