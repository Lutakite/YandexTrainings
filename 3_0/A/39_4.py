n, k = map(int, input().split())
graph = dict()
A = list()
B = list()
for i in range(1,n+1):
    graph[i] = list()
for i in range(k):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    if b!=a and b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)
    if b==a and b not in graph[a]:     
        graph[a].append(a)
m = int(input())

def bfs(graph, visited, start):
    visited[start][0] = 0
    queue = list()
    queue.append([start, 0])
    while queue:
        ss = queue.pop(0)
        s = ss[0]
        r = ss[1] + 1
        for neighbor in graph[s]:
            if r%2==0 and visited[neighbor][0] == 1000000:
                visited[neighbor][0] = r
                queue.append([neighbor,r])
            elif r%2==1 and visited[neighbor][1] == 1000000:
                visited[neighbor][1] = r
                queue.append([neighbor,r])
if m == 1:
    print(0)
else:
    robots = list(map(int, input().split()))

    noWay = False
    visits = list()
    for robot in robots:
        if noWay:
            break
        visited = list()
        visited.append([1000000, 1000000])
        for i in range(1, n+1):
            visited.append([1000000, 1000000])
        #visited = [[1000000, 1000000]]*(n+1)
        #print(visited)
        bfs(graph, visited, robot)
        #print("visited")
        #print(visited)
        visits.append(visited)
        #print(visited)
        #max = 0
        #for robot2 in robots:
            #if visited[robot2] == -1:
                #noWay = True
                #break
            #if visited[robot2] > max:
            #    max = visited[robot2]
    #print(visits)
    #if noWay:
    #    print(-1)
    #else:
    ans = 1000000
    
    #print("ans")
    #print(ans)
    for i in range (1, n+1):
        lc = -1
        ln = -1
        for j in range (0,m):
            #print(visits[j][i][0])
            #print(visits[j][i][1])
            if visits[j][i][0] >= 0:
                lc = max(lc, visits[j][i][0])
                ln = max(ln, visits[j][i][1])
            #print(lc)
            #print(ln)
            #print()
        #print()
        #print(lc)
        #print(ln)
        if lc > 0:
            ans = min(ans, min(lc, ln))
    for i in range(0, k):
        c = 0
        for j in range (0, m):
            #print(j)
            c = max(c, min(min(visits[j][A[i]][0], visits[j][A[i]][1]), min(visits[j][B[i]][0], visits[j][B[i]][1]))+0.5)
            if c > ans:
                break
        ans = min(ans, c)
    if ans < 100000:   
        print(ans)
    else:
        print(-1)