n, m = map(int, input().split())
labirint = list()
visited = dict()
for i in range(n):
    labirint.append(input().split())
    for j in range(m):
        visited[(i,j)] = -1
        if labirint[i][j] == "1":
            visited[(i,j)] = -2
        elif labirint[i][j] == "2":
            visited[(i,j)] = -3
#print(visited)            
def getNeighbours1(s, labirint, n, m):
    #print(labirint)
    result = list()
    i = 0
    for i in range(n-s[0]):
        if labirint[s[0]+i][s[1]] == "1":
            i -= 1
            break
        if labirint[s[0]+i][s[1]] == "2":
            result.append((s[0]+i, s[1]))
    if i!= 0:
        result.append((s[0]+i, s[1]))
    
    i = 0
    for i in range(s[0]+1):
        if labirint[s[0]-i][s[1]] == "1":
            i -= 1
            break
        if labirint[s[0]-i][s[1]] == "2":
            result.append((s[0]-i, s[1]))
    if i!= 0:
        result.append((s[0]-i, s[1]))
    
    i = 0
    for i in range(m-s[1]):
        #print(s[0])
        #print(s[1]+i)
        #print(labirint[s[0]][s[1]+i])
        if labirint[s[0]][s[1]+i] == "1":
            i -= 1
            break
        if labirint[s[0]][s[1]+i] == "2":
            #print("here")
            result.append((s[0], s[1]+i))
    if i!= 0:
        result.append((s[0], s[1]+i))
    
    i = 0
    for i in range(s[1]+1):
        if labirint[s[0]][s[1]-i] == "1":
            i -= 1
            break
        if labirint[s[0]][s[1]-i] == "2":
            result.append((s[0], s[1]-i))
    if i!= 0:
        result.append((s[0], s[1]-i))
    return result
    
def bfs(start, visited, labirint, n, m):
    visited[start] = 0
    queue = list()
    queue.append(start)
    done = False
    while not done and queue:
        s = queue.pop(0)
        for neighbor in getNeighbours1(s, labirint, n, m):
            if done:
                break
            #print(neighbor)
            if visited[neighbor] == -1:
                visited[neighbor] = visited[s]+1
                queue.append(neighbor)
            if visited[neighbor] == -3:
                #print(neighbor)
                return visited[s]+1
                done == True
                break
            #print(visited)
start = (0, 0)
#print(getNeighbours1(start, labirint, n, m))
print(bfs(start, visited, labirint, n, m))
#print(visited)