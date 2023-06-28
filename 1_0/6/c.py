w, h, n = map(int, input().split())

max = n*max(w,h)
    
def find(w, h, max):
    l = 0
    r = max
    while l < r:
        m = (l + r) // 2
        if (m // h) * (m // w) >= n:
            r = m
        else:
            l = m + 1
    return l
    
print(find(w, h, max))