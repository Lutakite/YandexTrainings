n = int(input())
s = list(map(int, input().split()))

res = list()
trip = list()
res = [1]*n
trip = [-1]*n

#print(s)
max = 1
maxi = 0
maxtrip = list()

for i in range(1, n):
    for j in range(0, i):
        if s[j] < s[i]:
            if res[j]+1 > res[i]:
                res[i] = res[j]+1
                trip[i] = j
    if res[i] > max:
        max = res[i]
        maxi = i

#print(res)
#print(trip)        
while True:
    maxtrip.append(s[maxi])
    maxi = trip[maxi]
    if maxi == -1:
        #maxtrip.append(s[maxi])
        break

for i in range(len(maxtrip)-1,-1,-1):
    print(maxtrip[i], end=" ")