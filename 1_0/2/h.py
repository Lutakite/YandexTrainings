s = input().split()

if len(s) < 4:
    print(' '.join(s))
else:
    minusmin1 = 0
    minusmin2 = 0
    plusmax1 = -100002
    plusmax2 = -100002
    plusmax3 = -100002
    for i in s:
        ii = int(i)
        if ii < 0:
            if ii <= minusmin1:
                minusmin2 = minusmin1
                minusmin1 = ii
            elif ii <= minusmin2:
                minusmin2 = ii
        #if ii > 0:
        if ii >= plusmax1:
            plusmax3 = plusmax2
            plusmax2 = plusmax1
            plusmax1 = ii
        elif ii >= plusmax2:
            plusmax3 = plusmax2
            plusmax2 = ii
        elif ii >= plusmax3:
            plusmax3 = ii
    if minusmin1*minusmin2*plusmax1 > plusmax1*plusmax2*plusmax3:
        print(str(minusmin1)+" "+str(minusmin2)+" "+str(plusmax1))
    else:
        print(str(plusmax2)+" "+str(plusmax1)+" "+str(plusmax3))
        