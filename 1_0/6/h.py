n, k = map(int,input().split())
lk = list()
for _ in range(n):
    lk.append(int(input()))
    
def find(k, lk):
    #print(lk)
    l = 0
    r = 10000002
    while l < r:
        m = (l + r + 1) // 2
        #print("m="+str(m))
        result = 0
        for i in range(len(lk)):
            result += lk[i] // m
        #print(result)
        #print()
        if result < k:
            r = m - 1
        else:
            l = m
    return l
    
print(find(k,lk))