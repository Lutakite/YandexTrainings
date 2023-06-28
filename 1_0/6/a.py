n, k = map(int, input().split())
ns = list(map(int, input().split()))
ns.sort()
ks = list(map(int, input().split()))

def check(element, list):
    l = 0
    r = len(list)
    while l < r:
        m = (l + r) // 2
        if list[m] > element:
            r = m
        elif list[m] < element:
            l = m + 1
        else:
            return True
    return False
    
for i in ks:
    if check(i, ns):
        print("YES")
    else:
        print("NO")