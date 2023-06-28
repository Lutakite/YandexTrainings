#import sys
#sys.setrecursionlimit(200000)
def dfs(graph, visited, now, mark, result):
    visited[now] = (True, mark)
    markneig = not mark
    for neig in graph[now]:
        if not visited[neig][0]:
            dfs(graph, visited, neig, markneig, result)
        else:
            if visited[neig][1] != markneig:
                result = False
                #print("no")
    return result

def doGraph(towersR, r, n):
    r *= 2
    vs = dict()
    visited = list()
    for i in range(n):
        visited.append((False, False))
        vs[i] = list()
        for j in range(n):
            if towersR[i][j] <= r and towersR[i][j] > 0:
                vs[i].append(j)
        #visited.append((False, False))
        #if i not in vs:
        #    vs[i] = list()
        #for j in range(i+1, n):
        #    if towersR[i][j] <= r:
        #        if j not in vs:
        #            vs[j] = list()
        #        vs[i].append(j)
        #        vs[j].append(i)
    return vs, visited

def checkbigger(towersR, l, r, n):
    #print(list)
    #print("element="+str(element))
    e = 0.000000005
    res = list()
    while l < r and r-l > e/2:
        m = (l + r) / 2
        print("m="+str(m))
        vs, visited = doGraph(towersR, m, n)
        #print(vs)
        #print(vs)
        result = True
        for i in range(n):
            if visited[i][0] == False:
                result = dfs(vs, visited, i, False, result)
                if result == False:
                    #print(visited)
                    break
        print(result)
        #print(visited)
        if result == False:
            r = m# - e
        else:
            l = m + e
            res = visited
    #print(l+1)
    return l, res

n = int(input())
towers = list()
towersR = list()
maxR = 0
minR = 10000000000
for i in range(n):
    towers.append(list(map(int, input().split())))
    towersR.append([0]*n)
    for j in range(0, i):
        towersR[j][i] = ((towers[i][0] - towers[j][0])**2 + (towers[i][1] - towers[j][1])**2)**0.5
        towersR[i][j] = towersR[j][i]
        if towersR[i][j] > maxR:
            maxR = towersR[i][j]
            #print(maxR)
        if towersR[i][j] < minR:
            minR = towersR[i][j]
            #print(minR)
#print(towers)
#print(towersR)
r = maxR + 0.0000001
print(maxR)
print(minR)
result, res = checkbigger(towersR, 0, r, n)
#print(result)
#print("color")
#print(res)
#0.707106781186548
print("{:.10}".format(result))
for i in range(n):
    if res[i][1]:
        print(2, end=" ")
    else:
        print(1, end=" ")
    