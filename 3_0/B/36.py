n = int(input())
graph = dict()
visited = dict()
visited2 = dict()
r = list()
r2 = list()
for i in range(1, n+1):
    graph[i] = list()
    r.append([])
    r2.append([])
    line = input().split()
    #visited[i] = -1
    for j in range(0, n):
        if line[j] == "1":
            graph[i].append(j+1)
            
def bfs(graph, visited, node, r):
    visited[node] = 0
    #print(r)
    r[0].append(node)
    queue = list()
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited[neighbor] = visited[s] + 1
                r[visited[s] + 1].append(neighbor)
                queue.append(neighbor)
first, last = map(int, input().split())
#print(graph)
bfs(graph, visited, first, r)
if last in visited:
    print(visited[last])
    if visited[last] != 0:
        bfs(graph, visited2, last, r2)
        print(first, end=" ")
        for i in range(1, visited[last]):
            #print("i="+str(i))
            #print(r[i])
            j = visited[last] - i
            #print("j="+str(j))
            #print(r2[j])
            found = False
            for k in r[i]:
                if found:
                    break
                for kk in r2[j]:
                    if k == kk:
                        print(k, end=" ")
                        found = True
                        break
        print(last)    
        #print(r)
        #print(r2)
else:
    print(-1)

