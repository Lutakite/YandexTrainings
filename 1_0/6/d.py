n, a, b, w, h = map(int, input().split())

max = max(w,h)
   
def countrec(a, w):
    return w // a

def find(n, a, b, w, h):
    l = 0
    r = max
    #print("max="+str(max))
    while l < r:
        m = (l + r + 1) // 2
        #print("m="+str(m))
        #print(a+2*m)
        #print(b+2*m)
        #print(countrec(a + 2*m, w)*countrec(b + 2*m, h))
        #print()
        if countrec(a + 2*m, w)*countrec(b + 2*m, h) < n:
            r = m - 1
        else:
            l = m
            #print("!!!!")
            #print(l)
    return l

res1 = find(n, a, b, w, h)
res2 = find(n, a, b, h, w)
if res1 > res2:
    print(res1)
else:
    print(res2)