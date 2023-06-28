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
        visited[v1] = (False, 2)
    if v2 not in vs:
        vs[v2] = list()
        visited[v2] = (False, 2)
    vs[v1].append(v2)
    vs[v2].append(v1)

def dfs(graph, visited, now, mark, result):
    visited[now] = (True, mark)
    markneig = not mark
    for neig in graph[now]:
        if not visited[neig][0]:
            dfs(graph, visited, neig, markneig, result)
        else:
            if visited[neig][1] != markneig:
                result = False
                #print("no")
    return result

result = True
for v in visited:
    if visited[v][0] == False:
        result = dfs(vs, visited, v, False, result)
        if result == False:
            break

if result:
    print("YES")
else:
    print("NO")