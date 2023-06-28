n, k = map(int, input().split())

res = [0]*(n+1)
res[0] = 1
t = k+1
if k > n:
    t = n + 1
for i in range(1,t):
    for j in range(i):
        res[i] += res[j] 
#print(res)        
for i in range(k+1, n):
    for j in range(i-k, i):
        res[i] += res[j]          
print(res[n-1])