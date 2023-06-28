n = int(input())
vs = dict()
visited = dict()
for i in range(1, n+1):
    line = input().split()
    j = 1
    if i not in vs:
        vs[i] = list()
        visited[i] = 0
    for e in line:
        if e == '1':
            vs[i].append(j)
        j += 1
#print(vs)
def dfs(graph, visited, now, ans, ciclo, parent, parents):
    visited[now] = 1
    for neig in graph[now]:
        if visited[neig] == 0:
            ciclo, ans = dfs(graph, visited, neig, ans, ciclo, now, parents+[now])
        elif visited[neig] == 1 and parent != neig:
            ciclo = True
            ans = parents[parents.index(neig):]
            ans.append(now)
            #print(ans)
            #print(parents)
            #print(now)
            #print(neig)
    visited[now] = 2
    return ciclo, ans


answered = False
ciclo = False
for ver in visited:
    if visited[ver] == 0:
        ans = list()
        ciclo = False
        ciclo, ans = dfs(vs, visited, ver, ans, ciclo, 0, [0])#, ciclovisited)
        #print(ans)
        if ciclo:
            answered = True
            print("YES")
            print(len(ans))
            for a in ans:
                print(a, end=" ")
            break
if answered == False:
    print("NO")