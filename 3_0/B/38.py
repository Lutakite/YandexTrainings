n, m, s, t, q = map(int, input().split())

start = (s, t)
nexts = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

visited = dict()
for i in range(1, n+1):
    for j in range(1, m+1):
        visited[(i,j)] = -1

visited[start] = 0
queue = list()
queue.append(start)
while queue:
    s = queue.pop(0)
    for neighbor in nexts:
        neignode = (s[0]+neighbor[0],s[1]+neighbor[1])
        if neignode in visited:
            if visited[neignode] == -1:
                visited[neignode] = visited[s] + 1
                queue.append(neignode)
result = 0            
for i in range(q):
    x, y = map(int, input().split())
    result += visited[(x, y)]
    if visited[(x,y)] == -1:
        result = -1
        break
print(result)
    