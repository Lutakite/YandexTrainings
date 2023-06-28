n, k = map(int, input().split())
graph = dict()
tunnels = dict()
for i in range(1,n+1):
    tunnels[i] = list()
    graph[i] = list()
for i in range(n+1, n+k+1):
    graph[i] = list()
P = n+1
#print(graph)
for i in range(k):
    a, b = map(int, input().split())
    #print(P)
    if b!=a and b not in tunnels[a]:
        graph[a].append(P)
        graph[P].append(a)
        graph[P].append(b)
        graph[b].append(P)
        tunnels[a].append(b)
        tunnels[b].append(a)
        P += 1
    if b==a and b not in tunnels[a]:
        graph[a].append(P)
        graph[P].append(a)        
        tunnels[a].append(a)
        P += 1
#print(graph)
m = int(input())
robots = list(map(int, input().split()))

def bfs(graph, visited, start):
    visited[start] = 0
    queue = list()
    queue.append(start)
    while queue:
        s = queue.pop(0)
        for neighbor in graph[s]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[s] + 1
                queue.append(neighbor)

res = 1000000000000    
noWay = False
visits = dict()               
for robot in robots:
    #print(robot)
    if noWay:
        break
    visited = list()
    visited.append(-1)
    for i in range(1, n+k+1):
        visited.append(-1)
    #print("visited")
    #print(visited)
    bfs(graph, visited, robot)
    visits[robot] = visited
    #print(visited)
    #max = 0
    for robot2 in robots:
        if visited[robot2] == -1:
            noWay = True
            break
        #if visited[robot2] > max:
        #    max = visited[robot2]
#print(visits)
if noWay:
    print(-1)
else:
    #print(visits)
    for i in range(1, n+k+1):
        t = visits[robots[0]][i]
        add = 4
        if i > n:
            add = 2
        else:
            if i in tunnels[i]:
                add = 2
        if t < res:
            found = True
            for robot in robots:
                if visits[robot][i] != t:
                    
                    print(max(visits[robot][i],t))
                    print(min(visits[robot][i],t))
                    if (max(visits[robot][i],t) - min(visits[robot][i],t)) % add == 0:
                        t = max(visits[robot][i],t)
                    else:
                        found = False
                        break
                #print(i)
                #print(robot)
                #print(visits[robot])
                #print(visits[robot][i])
                #print()
                #
                #    print(t)
                #    print()
                #    print()
                #    found = False
                #    break
        if found:
            res = t
    if res%2 == 0:
        print(res//2)
    else:
        print(res//2+0.5)
    #if max % 2 == 0:
    #    print(max//2)
    #else:
    #    print(max//2+1)