n, R, c = map(int,input().split())
high = list()
for _ in range(n):
    high.append(int(input()))
    
high.sort()
 
def find(n, R, c, high):
    #print(high)
    l = 0
    r = 1000000002
    while l < r:
        m = (l + r) // 2
        #print("m="+str(m))
        result = 0
        i = 0
        while i < len(high) - c + 1:
            if high[i+c-1] - high[i] <= m:
                result +=1
                i += c
            else:
                i += 1
        #print(result)
        #print(R)
        #print()
        if result >= R:
            #print("!!!")
            r = m
        else:
            l = m + 1
    return l

if len(high) == 1:
    print("0")
else:
    print(find(n, R, c, high))