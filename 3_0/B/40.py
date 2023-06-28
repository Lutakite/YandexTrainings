n = int(input())
m = int(input())
lines = list()
visited = dict()
graph = dict()
for i in range(m):
    #lines.append(list())
    line = input().split()
    lines.append(line[1:])
    for j in range(1, int(line[0])+1):
        visited[line[j]] = -1
        if line[j] not in graph:
            graph[line[j]] = []
        graph[line[j]].append(i)
#print(lines[14])
#print(graph)
start, finish = input().split()
def bfs(graph, visited, node):
    visited[node] = 0
    rline = dict()
    currentLine = graph[node]
    for line in graph[node]:
        rline[line] = 0
    #print(rline)
    queue = list()
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for line in currentLine:
            for neighbor in lines[line]:
                if visited[neighbor] == -1:
                    for neigline in graph[neighbor]:
                        if neigline not in rline:
                            rline[neigline] = rline[line] + 1
                            currentLine.append(neigline)
                            #print(neigline)
                            #print(rline[neigline])
                            #print()
                    visited[neighbor] = rline[neigline]####
                    queue.append(neighbor)
                else:
                    visited[neighbor] = min(visited[neighbor], rline[line])
    #return count
res = bfs(graph, visited, start)
print(visited[finish])