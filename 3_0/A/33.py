#import sys
#sys.setrecursionlimit(200000)
def dfs(graph, visited, now, mark, result):
    visited[now] = (True, mark)
    for neig in graph[now]:
        if visited[neig][0] == False:
            result = dfs(graph, visited, neig, not mark, result)
        else:
            if visited[neig][1] == mark:
                result = False
                #print("no")
    return result

def doGraph(towersR, r, n):
    vs = dict()
    visited = list()
    for i in range(n):
        visited.append((False, False))
        if i not in vs:
            vs[i] = list()
        for j in range(i+1, n):
            if towersR[i][j] < r:#<=
                if j not in vs:
                    vs[j] = list()
                vs[i].append(j)
                vs[j].append(i)
    return vs, visited

def checkbigger(towersR, l, r, n, sortedTowersR):
    #print(list)
    #print("element="+str(element))
    res = list()
    while l < r:# and r < len(sortedTowersR):# and r - l > 1:
        m = (l + r + 1) // 2
        #print("m="+str(m))
        #print(sortedTowersR[m])
        vs, visited = doGraph(towersR, sortedTowersR[m], n)
        length = 0
        for v in vs:
            #print(vs[v])
            length += len(vs[v])
        #print(length)
        #print(visited)
        #print(vs)
        result = True
        for i in range(n):
            if visited[i][0] == False:
                result = dfs(vs, visited, i, False, result)
                #print(result)
                if result == False:
                    break
        #print(result)
        #print(visited)
        if result == False:
            r = m - 1# - e
        else:
            l = m# + 1
            res = visited
    #print(l+1)
    return sortedTowersR[l], res

n = int(input())
towers = list()
towersR = list()
sortedTowersR = set()
maxR = 0
for i in range(n):
    towers.append(list(map(int, input().split())))
    towersR.append([0]*n)
    for j in range(0, i):
        towersR[j][i] = (towers[i][0] - towers[j][0])**2 + (towers[i][1] - towers[j][1])**2
        towersR[i][j] = towersR[j][i]
        sortedTowersR.add(towersR[i][j])
        if towersR[i][j] > maxR:
            maxR = towersR[i][j]

sortedTowersR = sorted(sortedTowersR)
#print(sortedTowersR)
r = len(sortedTowersR) - 1
#print(r)
#print(sortedTowersR[r-1])
#print(maxR)
#result, res = checkbigger(towersR, 0, 43, n, sortedTowersR)
result, res = checkbigger(towersR, 0, r, n, sortedTowersR)
#print(result)
#print("color")
#print(res)
#0.707106781186548
print("{:.20}".format(result**0.5/2))
for i in range(n):
    if res[i][1]:
        print(2, end=" ")
    else:
        print(1, end=" ")
    