n = int(input())

res = list()
res.append(0)
res.append(0)
trip = list()
trip.append(0)
trip.append(1)

for i in range(2,n+1):
    t1 = 1000000002
    t2 = 1000000002
    if i % 2 == 0:
        t1 = res[i//2] + 1
    if i % 3 == 0:
        t2 = res[i//3] + 1
    min = res[i-1] + 1
    trip.append(i-1)
    if t1 < min:
        min = t1
        trip[i] = i//2
    if t2 < min:
        min = t2
        trip[i] = i//3
    
    res.append(min)

#print(res)
#print(trip)
print(res[n])

result = list()
result.append(n)
i = n
while i > 1:
    result.append(trip[i])
    i = trip[i]
    
for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")