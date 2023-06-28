m = int(input())
n = int(input())

sectors = {}
for i in range(n):
    a, b = map(int, input().split())
    todel = list()
    for sector in sectors:
        if (sectors[sector][0] <= a and sectors[sector][1] >= a) or (sectors[sector][0] <= b and sectors[sector][1] >= b) or (sectors[sector][0] >= a and sectors[sector][1] <= b):
            todel.append(sector)
    for t in todel:
        del sectors[t]
    sectors[i] = (a, b)
print(len(sectors))
