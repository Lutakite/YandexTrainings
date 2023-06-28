n = int(input())
graph = dict()
visited = dict()

start = -1
for i in range(0, n):
    input()
    for j in range(0, n):
        line = input()
        for k in range(0, n):
            v = (i, j, k)
            if v not in graph:
                graph[v] = list()
            if line[k] == '.':
                visited[v] = -1
            elif line[k] == 'S':
                visited[v] = -1
                start = v
            else:
                visited[v] = -2
            neig = list()
            if j > 0:
                neig.append((i, j-1, k))
            if j < n-1:
                neig.append((i, j+1, k))
            if k > 0:
                neig.append((i, j, k-1))
            if k < n-1:
                neig.append((i, j, k+1))
            if i > 0:
                neig.append((i-1, j, k))
            if i < n-1:
                neig.append((i+1, j, k))
            for neighbor in neig:
                graph[v].append(neighbor)

#print(graph)
#print(visited)
    
            
def bfs(graph, visited, node):
    visited[node] = 0
    queue = list()
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for neighbor in graph[s]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[s] + 1
                queue.append(neighbor)

bfs(graph, visited, start)

min = n*n*n+1
for i in range(n):
    for j in range(n):
        v = visited[(0,i,j)]
        if v >= 0 and v < min:
            min = v
print(min)
#print(visited)
#if last in visited:
#    print(visited[last])
#else:
#    print(-1)

