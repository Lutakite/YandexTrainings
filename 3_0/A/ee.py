n, m = map(int, input().split())
from collections import deque

labirint = list()
visited = dict()
for i in range(n):
    labirint.append(input())
    #print(labirint)
    for j in range(m):
        visited[(i,j)] = -1
        if labirint[i][j] == "X":
            visited[(i,j)] = -2
        #elif labirint[i][j] == "2":
        #    visited[(i,j)] = -3
#print(visited)            
def getNeighbours1(s, labirint, n, m):
    result = list()
    i = 1
    while s[0]-i >= 0:
        if labirint[s[0]-i][s[1]] == "X":
            break
        result.append((s[0]-i, s[1]))
        i += 1
        
    i = 1
    while s[0]+i < n:
        if labirint[s[0]+i][s[1]] == "X":
            break
        result.append((s[0]+i, s[1]))
        i += 1
        
    i = 1
    while s[1]-i >= 0:
        if labirint[s[0]][s[1]-i] == "X":
            break
        result.append((s[0], s[1]-i))
        i += 1
        
    i = 1
    while s[1]+i < m:
        if labirint[s[0]][s[1]+i] == "X":
            break
        result.append((s[0], s[1]+i))
        i += 1
        
    i = 1
    while s[0]+i < n and s[1]+i < m:
        if labirint[s[0]+i][s[1]+i] == "X":
            break
        result.append((s[0]+i, s[1]+i))
        i += 1
        
    i = 1
    while s[0]-i >= 0 and s[1]-i >= 0:
        if labirint[s[0]-i][s[1]-i] == "X":
            break
        result.append((s[0]-i, s[1]-i))
        i += 1
        
    i = 1
    while s[0]-i >= 0 and s[1]+i < m:
        if labirint[s[0]-i][s[1]+i] == "X":
            break
        result.append((s[0]-i, s[1]+i))
        i += 1
        
    i = 1
    while s[0]+i < n  and s[1]-i >= 0:
        if labirint[s[0]+i][s[1]-i] == "X":
            break
        result.append((s[0]+i, s[1]-i))
        i += 1
    return result
#print(labirint)
#print(labirint[0])
#print(labirint[0][0])
#print(len(labirint))
#print(len(labirint[0]))
s0, s1 = map(int, input().split())
start = (n-s1, s0-1)    
f0, f1 = map(int, input().split())
finish = (n-f1, f0-1)
labirint[n-f1] = labirint[n-f1][:(f0-1)] + "Y" + labirint[f1-1][f0:] 
#print(finish)
#print(getNeighbours1((4,0),labirint, n,m))

def bfs(start, visited, labirint, n, m):
    visited[start] = 0
    queue = deque()
    queue.append(start)
    done = False
    while not done and queue:
        s = queue.popleft()
        #print("s=")
        #print(s)
        for neighbor in getNeighbours1(s, labirint, n, m):
            #if done:
            #    break
            if visited[neighbor] == -1:
                visited[neighbor] = visited[s]+1
                #print(neighbor)
                #print(visited[neighbor])
                queue.append(neighbor)
            if neighbor == finish:
            #    #print(neighbor)
            #   return visited[s]+1
                done == True
                break
            #print(visited)
#print(getNeighbours1(start, labirint, n, m))
bfs(start, visited, labirint, n, m)
if visited[finish] != 0:
    print(visited[finish])
else:
    print(1)