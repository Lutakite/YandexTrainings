n, a, b = map(int, input().split())

maxprice = max(a,b)
minprice = min(a,b)
f = [maxprice*n]*(n+1)

f[0] = 0
f[1] = 0
if n > 1:
    f[2] = maxprice

for i in range(3, n+1):
    for j in range(1, i):
        res = min(max(maxprice+f[i-j], minprice+f[j]), max(minprice+f[i-j], maxprice+f[j]))
        if res < f[i]:
            f[i] = res
            
print(f[n])

