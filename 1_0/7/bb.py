n, m = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)
    a.append([x, '('])
    a.append([y, ')'])
print(a)

m = list(map(int, input().split()))
for i in range(len(m)):
    a.append([m[i], '(('])
    
print(a)
k = 0
a.sort()
print(a)
dict = {}
for i in range(len(a)):
    if a[i][1] == '(':
        k += 1
    elif a[i][1] == ')':
        k -= 1
    else:
        dict[a[i][0]] = k
for i in m:
    print(dict[i], end=" ")