import sys
sys.setrecursionlimit(200000)

v, e = map(int, input().split())
    
vs = dict()
visited = dict()
#ciclovisited = dict()

for i in range(1, v+1):
    vs[i] = list()
    visited[i] = 0
    #ciclovisited[j] = 0

for _ in range(e):
    line = input().split()
    v1 = int(line[0])
    v2 = int(line[1])
    #if v1 not in vs:
    #    vs[v1] = list()
    #    visited[v1] = 0
    #if v2 not in vs:
    #    vs[v2] = list()
    #    visited[v2] = 0
    vs[v2].append(v1)

def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

if 1 in vs:
    dfs(vs, visited, 1)

    result = list()
    #print(visited)
    for i in visited:
        if visited[i] == True:
            result.append(i)

    #print(len(result))
    result.sort()
    for i in result:
        print(i, end=" ")
else:
    print(1)
    print(1)