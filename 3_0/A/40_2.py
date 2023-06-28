from collections import deque
n, k = map(int, input().split())
#visited = dict()
graph = dict()
components = dict()
maps = list()
globalvisited = dict()
towns = dict()
def dfs(graph, visited, now, ans):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            ans = dfs(graph, visited, neig, ans)
    ans.append(now)
    return ans

p = n + 1 #новые платные вершины    
for i in range(0,k):
    #print(i)
    m = int(input())
    maps.append(dict())
    visited = dict()
    for j in range(0, m):
        a, b = map(int, input().split())
        if a not in towns:
            towns[a] = list()
        if b not in towns:
            towns[b] = list()
        towns[a].append(i)
        towns[b].append(i)
        if a not in maps[i]:
            maps[i][a] = list()
            graph[(a,i)] = list()
            globalvisited[(a,i)] = -1
            visited[a] = False
        if b not in maps[i]:
            maps[i][b] = list()
            graph[(b,i)] = list()
            globalvisited[(b,i)] = -1
            visited[b] = False
        if b not in maps[i][a]:
            maps[i][a].append(b)
            maps[i][b].append(a)
            graph[(a,i)].append((b,i))
            graph[(b,i)].append((a,i))
    for v in maps[i]:
        if visited[v] == False:
            ans = list()
            ans = dfs(maps[i], visited, v, ans)
            graph[(p,0)] = list()
            globalvisited[(p,0)] = -1
            for a in ans:
                graph[(a,i)].append((p,0))
                graph[(p,0)].append((a,i))
                if a not in components:
                    components[a] = dict()
                components[a][i] = p
            p += 1
maps = []
#print()
#print(components)
#print()
#print(towns)
#print(graph)
for town in towns:
    #if town == 1:
        #print(town)
    #print(towns[town])
    for map in towns[town]:
        for map2 in towns[town]:
            if map == map2:
                continue
            #print(town)
            #print(map)
            #print(components[town][map2])
            #print()
            graph[(town, map)].append((components[town][map2],0))
            #graph[(components[town][map2],0)].append((town, map))
            #print(components[town][map])
#print(graph)
components = []
queue = deque()
for i in towns[1]:
    queue.append((1,i))
    globalvisited[(1,i)] = 0
towns = []
done = False
ans = 0
g = 1
nextmapqueue = deque()
while not done and (queue or nextmapqueue):
    if len(queue) == 0:
        queue = nextmapqueue
        nextmapqueue = deque()
        #print(queue)
        g += 1
        #print(g)
    #print("queue")
    #print(queue)
    #print("nextmapqueue")
    #print(nextmapqueue)
    s = queue.popleft()
    #print(s)
    #print(graph[s])
    for neighbor in graph[s]:
        if done:
            break
        if globalvisited[neighbor] == -1:
            #print(neighbor)
            if neighbor[0] > n:
                nextmapqueue.append(neighbor)
            else:
                queue.append(neighbor)
            globalvisited[neighbor] = g
            #else:
                #queue.appendleft(neighbor)
            #elif neighbor[0] == n:
            if neighbor[0] == n:
                done = True
                ans = globalvisited[neighbor]
                break
        #print(globalvisited[neighbor])
#print(globalvisited)
if done:
    print(ans)
else:
    print(-1)