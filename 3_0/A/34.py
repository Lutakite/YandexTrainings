#import sys
#sys.setrecursionlimit(200000)
from collections import deque
n, m = map(int, input().split())

def dfs(graph, visited, now, count, min, heights, visits):
    visited[now] = True
    visits += 1
    for neig in graph[now]:
        if not visited[neig]:
            if heights[neig] == min:
                count.append((min, neig))
            count, visits = dfs(graph, visited, neig, count, min, heights, visits)
    return count, visits

field = list()
k = 1
vs = dict()
visited = dict()
heights = dict()
listheight = list()
#field.append([10002]*m)
for i in range(n):
    field.append(list())
    line = input().split()
    #field[i].append(10002)
    for j in range(m):
        field[i].append(k)
        listheight.append((int(line[j]),k))
        heights[k] = int(line[j])
        vs[k] = list()
        visited[k] = False
        k += 1 
    #field[i].append(10002)
#field.append([10002]*m)
#print(field)
for i in range(n):
    for j in range(m):
        vs[field[i][j]] = list()
        if i > 0:
            if heights[field[i][j]] <= heights[field[i-1][j]]:
                vs[field[i][j]].append(field[i-1][j])
        if i < n-1:
            if heights[field[i][j]] <= heights[field[i+1][j]]:
                vs[field[i][j]].append(field[i+1][j])
        if j > 0:
            if heights[field[i][j]] <= heights[field[i][j-1]]:
                vs[field[i][j]].append(field[i][j-1])
        if j < m-1:
            if heights[field[i][j]] <= heights[field[i][j+1]]:
                vs[field[i][j]].append(field[i][j+1])
#print(vs)
result = 0
visits = 0
listheight.sort()
newlistheight = deque()
for i in listheight:
    newlistheight.append(i)
#print(newlistheight)
globalcount = deque()
while visits < m*n:
    #print(newlistheight)
    min, a = newlistheight.popleft()
    while len(globalcount) > 0 and globalcount[0] == (min, a):
        #print("popping")
        #print(a)
        globalcount.popleft()
        min, a = newlistheight.popleft()
        
        
    if visited[a] == True:
        continue
    count, visits = dfs(vs, visited, a, [], min, heights, visits)
    count.sort()
    globalcount += count
    #print(a)
    #print(min)
    #print(count)
    #print(visits)
    #print()
    result += 1
    #result += count
    #for _ in range(len(count)):
    #    newlistheight.popleft()
        
print(result)