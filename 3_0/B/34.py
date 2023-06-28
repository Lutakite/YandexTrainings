import sys
sys.setrecursionlimit(200000)

v, e = map(int, input().split())
    
vs = dict()
visited = dict()
#ciclovisited = dict()

for i in range(1, v+1):
    j = str(i)
    vs[j] = list()
    visited[j] = 0
    #ciclovisited[j] = 0

for _ in range(e):
    line = input().split()
    v1 = line[0]
    v2 = line[1]
    #if v1 not in vs:
    #    vs[v1] = list()
    #    visited[v1] = 0
    #if v2 not in vs:
    #    vs[v2] = list()
    #    visited[v2] = 0
    vs[v1].append(v2)

def dfs(graph, visited, now, ans, ciclo):#, ciclovisited):
    visited[now] = 1
    #ciclovisited[now] = 1
    for neig in graph[now]:
        if visited[neig] == 0:
            ciclo = dfs(graph, visited, neig, ans, ciclo)#, ciclovisited)
        if visited[neig] == 1:
        #elif ciclovisited[neig] == 1:
            #print(now)
            #print(neig)
            ciclo = True
            #print("!!!")
    visited[now] = 2
    #ciclovisited[now] = 2
    ans.append(now)
    return ciclo

ans = list()
ciclo = False
for ver in visited:
    if visited[ver] == 0:
        #ciclovisited = dict()
        #for i in range(1, v+1):
        #    j = str(i)
        #    ciclovisited[j] = 0
        #print(ciclovisited)
        ciclo = False
        ciclo = dfs(vs, visited, ver, ans, ciclo)#, ciclovisited)
        #print(ciclo)
        if ciclo:
            #print("!!!")
            break
if ciclo:
    print("-1")
else:
    print(' '.join(reversed(ans)))