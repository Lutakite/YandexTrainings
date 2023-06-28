from collections import deque
n, k = map(int, input().split())

components = dict()
graphComponents = dict()
visitedComponents = dict()

start = deque()
finish = set()
class BitSet:
    cell_len = 32

    def __init__(self, n):
        self.storage = [0] * (n//self.cell_len + 1)
        self.items = []

    def add(self, n):
        if not self.get(n):
            self.items.append(n)
        cell_idx, bit_idx = n // self.cell_len, n % self.cell_len
        self.storage[cell_idx] |= 1 << bit_idx

    def get(self, n):
        cell_idx, bit_idx = n // self.cell_len, n % self.cell_len
        return ((self.storage[cell_idx] >> bit_idx) & 1) == 1
        
def dfs(graph, visited, now, ans):
    visited[now] = True
    for neig in graph[now].items:
        if not visited[neig]:
            ans = dfs(graph, visited, neig, ans)
    ans.add(now)
    return ans

p = n + 1 #новые платные вершины    
for i in range(0,k):
    m = int(input())
    mapi = dict()
    visited = dict()
    for j in range(0, m):
        a, b = map(int, input().split())
        if a not in mapi:
            mapi[a] = BitSet(n)
            visited[a] = False
        if b not in mapi:
            mapi[b] = BitSet(n)
            visited[b] = False
        if mapi[a].get(b)==0:
            mapi[a].add(b)
            mapi[b].add(a)
    for v in mapi:
        if visited[v] == False:
            ans = BitSet(n)
            ans = dfs(mapi, visited, v, ans)
            #visitedComponents[p] = -1
            for a in ans.items:
                if a == 1:
                    start.append(p)
                    visitedComponents[p] = 0
                elif a == n:
                    finish.add(p)
                if a not in components:
                    components[a] = dict()
                components[a][i] = p
            p += 1
            
for town in components:
    for map1 in components[town]:
        p1 = components[town][map1]
        if p1 not in graphComponents:
            graphComponents[p1] = BitSet(p)
        for map2 in components[town]:
            if map1 == map2:
                continue
            p2 = components[town][map2]
            if p2 not in graphComponents:
                graphComponents[p2] = BitSet(p)
            if graphComponents[p2].get(p1)==0:
                graphComponents[p1].add(p2)
                graphComponents[p2].add(p1)
            
#print(graphComponents)
#print(start)
#print(finish)     
#queue = start
done = False
while not done and start:
    s = start.popleft()
    for neighbor in graphComponents[s].items:
        if neighbor not in visitedComponents:
            visitedComponents[neighbor] = visitedComponents[s]+1
            start.append(neighbor)
        if neighbor in finish:
            ans = visitedComponents[neighbor]
            done = True
            break
if done:
    print(ans+1)
else:
    print(-1)