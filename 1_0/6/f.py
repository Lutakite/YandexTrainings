n, x, y = map(int, input().split())

max = 100000000000
   
if x > y:
    x, y = y, x

def find(n,x,y):
    l = 0
    r = max
    while l < r:
        m = (l + r) // 2
        #print("seconds:" + str(m))
        #print("papers:" + str(m // x + ((m-x) // y)))
        if m // x + ((m-x) // y) >= n:
            r = m
        else:
            l = m + 1
    return l

print(find(n,x,y))