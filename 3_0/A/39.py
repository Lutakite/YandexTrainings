n, k = map(int, input().split())
graph = dict()
#visited = dict()
for i in range(1,n+1):
    graph[i] = list()
for i in range(k):
    a, b = map(int, input().split())
    if b!=a and b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)
    if b==a and b not in graph[a]:
        graph[a].append(b)
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

max = 0    
noWay = False               
for robot in robots:
    if noWay:
        break
    visited = dict()
    for i in range(1, n+1):
        visited[i] = -1
    #print("visited")
    #print(visited)
    bfs(graph, visited, robot)
    #print(visited)
    #max = 0
    for robot2 in robots:
        if visited[robot2] == -1:
            noWay = True
            break
        if visited[robot2] > max:
            max = visited[robot2]
if noWay:
    print(-1)
else:
    
    if max % 2 == 0:
        print(max//2)
    else:
        print(max//2+1)