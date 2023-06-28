n = 8

def returnNum(s):
    if s == 'a':
        return 1
    elif s == 'b':
        return 2
    elif s == 'c':
        return 3
    elif s == 'd':
        return 4
    elif s == 'e':
        return 5
    elif s == 'f':
        return 6
    elif s == 'g':
        return 7
    elif s == 'h':
        return 8

line = input().split()
start1 = (returnNum(line[0][0]),int(line[0][1]))
start2 = (returnNum(line[1][0]),int(line[1][1]))

visited1 = dict()
visited2 = dict()

nexts = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

def bfs(visited, start):
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
                    
for i in range(1, n+1):
    for j in range(1, n+1):
        visited1[(i,j)] = -1
        visited2[(i,j)] = -1

visited1[start1] = 0
visited2[start2] = 0
bfs(visited1, start1)
bfs(visited2, start2)
found = False
res = -1
for i in range(1, n+1):
    for j in range(1, n+1):
        if visited1[(i,j)] != -1 and visited1[(i,j)] == visited2[(i,j)]:
            if not found:
                #print(visited1[(i,j)])
                res = visited1[(i,j)]
                found = True
            else:
                res = min(res, visited1[(i,j)])
print(res)