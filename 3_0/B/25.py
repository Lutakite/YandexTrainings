n = int(input())

s = list(map(int, input().split()))
s.sort()

res = list()
res.append(0)
res.append(s[1]-s[0])
if n > 2:
    res.append(s[2]-s[0])

for i in range(3, n):
    #print("i="
    res.append(min(res[i-2], res[i-1])+s[i]-s[i-1])
    
#print(res)
print(res[n-1])