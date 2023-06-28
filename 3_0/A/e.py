n, m = map(int, input().split())
from collections import deque
from collections import defaultdict

labirint = list()
def make3d(x):
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append([x] * 8)
    return result

distance = make3d(-1)
#distance = defaultdict(lambda: -1)
for i in range(n):
    labirint.append(input())
    #for j in range(m):
        #distance[(i,j)] = -1
        #if labirint[i][j] == "X":
        #    distance[(i,j)] = -2



d = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
def getNeig(s, labirint, n, m, d):
    x, y, z = s
    nx = x + d[z][0]
    ny = y + d[z][1]
    if nx >= 0 and nx < n and ny >= 0 and ny < m and labirint[nx][ny] != 'X':
        result = [(0, (nx, ny, z))]
    else:
        result = list()
    for i in range(len(d)):
        result.append((1, (x, y, i)))
    return result
    
s0, s1 = map(int, input().split())
start = [(n-s1, s0-1, i) for i in range(len(d))]
f0, f1 = map(int, input().split())
finish = [(n-f1, f0-1, i) for i in range(len(d))]
result = -1

def _get(x, arr):
    #print(arr[x[0]][x[1]][x[2]])
    return arr[x[0]][x[1]][x[2]]

def _set(x, arr, v):
    arr[x[0]][x[1]][x[2]] = v

def bfs(start, distance, labirint, n, m):
    global result
    queue = deque()
    for s in start:
        _set(s, distance, 1)
        queue.append(s)
    done = False
    reallydistance = make3d(False)
    while not done and queue:
        s = queue.popleft()
        if _get(s, reallydistance):
            continue
        else:
            _set(s, reallydistance, True)
        #if distance[s] != -1:
        #    continue
        #print("s=",end="")
        #print(s)
        for weight, neighbor in getNeig(s, labirint, n, m, d):
            if _get(neighbor, distance) == -1 or _get(s, distance) + weight < _get(neighbor, distance):
                #print(neighbor)
                _set(neighbor, distance, _get(s, distance) + weight)
                #print(distance[neighbor])
                if weight != 0:
                    queue.append(neighbor)
                else:
                    queue.appendleft(neighbor)
            #if neighbor in finish:
            #    #print("!!!!")
            #    done == True
             #   result = distance[neighbor]
                #print(result)
             #   return
bfs(start, distance, labirint, n, m)

print(min(_get(i, distance) for i in finish))
#if result == 0:
#    print(1)
#else:
#print(result)
#print(finish)
#print(distance[(0,5,0)])
