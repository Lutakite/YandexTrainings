n = int(input())
a = list()
b = list()
c = list()
res = list()

a.append(11000)
b.append(11000)
c.append(11000)

a.append(11000)
b.append(11000)
c.append(11000)

a.append(11000)
b.append(11000)
c.append(11000)

for _ in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

res.append(0)
res.append(0)
res.append(0)

#print(a)
#print(res)
for i in range(3, n+3):
    res.append(min(res[i-1]+a[i], res[i-2]+b[i-1], res[i-3]+c[i-2]))
    
print(res[n+2])