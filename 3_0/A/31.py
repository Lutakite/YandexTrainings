labirint = list()

k = 1  
vs = dict()
visited = dict()
n = int(input())
for i in range(n):
    labirint.append(list())
    line = input()
    for j in range(n):
        if line[j]=="*":
            labirint[i].append(0)
        else:
            labirint[i].append(k)
            vs[k] = list()
            visited[k] = False
            k += 1

#print(labirint)          

for i in range(1, n-1):
    for j in range(1, n-1):
        if labirint[i][j] != 0:
            if labirint[i-1][j] != 0:
                vs[labirint[i][j]].append(labirint[i-1][j])
            if labirint[i+1][j] != 0:
                vs[labirint[i][j]].append(labirint[i+1][j])
            if labirint[i][j-1] != 0:
                vs[labirint[i][j]].append(labirint[i][j-1])
            if labirint[i][j+1] != 0:
                vs[labirint[i][j]].append(labirint[i][j+1])
            
i, j = map(int, input().split())

def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

dfs(vs, visited, labirint[i-1][j-1])

result = list()
for i in visited:
    if visited[i] == True:
        result.append(i)

print(len(result))