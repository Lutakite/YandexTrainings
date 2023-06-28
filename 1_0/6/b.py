n, k = map(int, input().split())
ns = list(map(int, input().split()))
ks = list(map(int, input().split()))

def checkbigger(element, list):
    l = 0
    r = len(list) - 1
    while l < r and l < len(list):
        m = (l + r) // 2
        if list[m] >= element:
            r = m
        elif list[m] < element:
            l = m + 1
    return list[l]
    
def checksmaller(element, list):
    l = 0
    r = len(list) - 1
    while l < r and r :
        m = (l + r + 1) // 2
        if list[m] > element:
            r = m - 1
        elif list[m] <= element:
            l = m
    return list[l]
    
for i in ks:
    n1 = checkbigger(i, ns)
    n2 = checksmaller(i, ns)
    if abs(n2-i) <= abs(n1-i):
        print(n2)
    else:
        print(n1)