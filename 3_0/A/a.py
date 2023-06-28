from collections import deque
n = int(input())
poezd = deque()
vagon = dict()
for _ in range(n):
    line = input().split()
    if line[0] == 'add':
        k = int(line[1])
        if line[2] not in vagon:
            vagon[line[2]] = 0
        vagon[line[2]] += k
        poezd.append((line[2], k))
    elif line[0] == 'delete':
        k = int(line[1])
        while poezd[-1][1] < k:
            kk = poezd[-1][1]
            k -= kk
            #print(k)
            vagon[poezd.pop()[0]] -= kk
        if k > 0:
            poezd[-1] = (poezd[-1][0], poezd[-1][1] - k)
            vagon[poezd[-1][0]] -= k
    elif line[0] == 'get':
        print(vagon.get(line[1],0))
    #print(vagon)
    #print(poezd)
        