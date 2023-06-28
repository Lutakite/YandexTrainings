from collections import deque
n, k = map(int, input().split())
visited = dict()
roads = dict()
ro = list()
ro.append({})
for i in range(1, n+1):
    roads[(i, 0)] = dict()
    visited[(i, 0)] = False
    ro.append({})
    #ro[i] = dict()
    ro[i][0] = 1000000000
    #ro[(i, 0)] = 1000000000
for i in range(1,k+1):
    m = int(input())
    for j in range(0, m):
        a, b = map(int, input().split())
        if (a, i) not in roads:
            roads[(a, i)] = dict()
            visited[(a, i)] = False
            ro[a][i] = 1000000000
            #ro[(a, i)] = 1000000000
            roads[(a, i)][(a, 0)] = 0
            roads[(a, 0)][(a, i)] = 1
        if (b, i) not in roads:
            roads[(b, i)] = dict()
            visited[(b, i)] = False
            ro[b][i] = 1000000000
            #ro[(b, i)] = 1000000000
            roads[(b, i)][(b, 0)] = 0
            roads[(b, 0)][(b, i)] = 1
        roads[(a, i)][(b, i)] = 0
        roads[(b, i)][(a, i)] = 0
#ro[(1,0)] = 0
ro[1][0] = 0
deq = deque()
deq.appendleft((1,0))
while deq:
    s = deq.popleft()
    if visited[s] == False:
        for neighbor in roads[s]:
            needAppend = False
            price = 0
            if visited[neighbor] == False:
                #r = ro[s] + roads[s][neighbor]
                r = ro[s[0]][s[1]] + roads[s][neighbor]
                if r < ro[neighbor[0]][neighbor[1]]:#r < ro[neighbor]:
                    needAppend = True
                    #ro[neighbor] = r
                    ro[neighbor[0]][neighbor[1]] = r
                    price = roads[s][neighbor]
            if needAppend:
                if price == 0:
                    deq.appendleft(neighbor)
                else:
                    deq.append(neighbor)
        visited[s] = True
if ro[n][0] != 1000000000:#ro[(n, 0)] != 1000000000:
    print(ro[n][0])#(ro[(n, 0)])  
else:
    print(-1)