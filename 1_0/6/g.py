n = int(input())
M = int(input())
t = int(input())

#x*2*n + (m-2*x)*2 <= t
if M > n:
    n, M = M, n
def find(n, M, t):
    l = 0
    r = M//2
    #print(r)
    while l < r:
        m = (l + r + 1) // 2
        #print("m="+str(m))
        #print(str(2*n*m + 2*M*m - 4*m*m))
        #print()
        if 2*n*m + 2*M*m - 4*m*m > t:
            r = m - 1
        else:
            l = m
    return l
    
print(find(n, M, t))