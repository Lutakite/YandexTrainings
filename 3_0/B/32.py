import sys
sys.setrecursionlimit(200000)

v, e = map(int, input().split())

vs = dict()
visited = dict()

result = set()

for _ in range(e):
    line = input().split()
    v1 = int(line[0])
    v2 = int(line[1])
    if v1 not in vs:
        vs[v1] = list()
        visited[v1] = False
    if v2 not in vs:
        vs[v2] = list()
        visited[v2] = False
    vs[v1].append(v2)
    vs[v2].append(v1)

def dfs(graph, visited, now, ans, i):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, ans, i)
    ans[i].append(now)

resultcomponents = list()
j = 0
for i in range(1, v+1):
    if i in vs and visited[i] == False:
        resultcomponents.append(list())
        dfs(vs, visited, i, resultcomponents, j)
        j += 1   
    elif i not in vs:
        resultcomponents.append(list())
        resultcomponents[j].append(i)
        j += 1   
   
    
print(len(resultcomponents))
for result in resultcomponents:
    print(len(result))
    for r in result:
        print(r, end=" ")
    print()