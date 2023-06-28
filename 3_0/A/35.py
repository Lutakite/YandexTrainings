n = int(input())
#clubs = list()
graph = dict()
visited = dict()
countin = dict()

heap = list()
heap.append(0)

def add2heap(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i//2 > 0 and heap[i // 2] > x:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        i = i//2
    
def getfromheap(heap):
    res = heap[1]
    heap[1] = heap[len(heap)-1]
    i = 1
    while i*2 < len(heap):
        if ((i*2+1 < len(heap) and heap[i*2] <= heap[i*2+1]) or i*2+1 == len(heap)) and heap[i*2] < heap[i]:
            heap[i*2], heap[i] = heap[i], heap[i*2]
            i = i*2
        elif i*2+1 < len(heap) and heap[i*2] > heap[i*2+1] and heap[i*2+1] < heap[i]: 
            heap[i*2+1], heap[i] = heap[i], heap[i*2+1]
            i = i*2+1
        else:
            break
    heap.pop()
    return res 

for i in range(1, n+1):
    visited[i] = False
    if i not in graph:
        graph[i] = list()
    c = list(map(int, input().split()))
    countin[i] = c[0]
    if c[0] == 0:
        add2heap(heap, i)
    for j in range(1, c[0]+1):
        if c[j] not in graph:
            graph[c[j]] = list()
        graph[c[j]].append(i)
#print(graph)
while len(heap) > 1:
    #print(heap)
    club = getfromheap(heap)
    #print(graph[club])
    for nextclub in graph[club]:
        #print(nextclub, end=" ")
        #print(countin[nextclub])
        countin[nextclub] -= 1
        if countin[nextclub] == 0:
            add2heap(heap, nextclub)
    #print(countin)
    #print(graph[club])
    print(club, end = " ")
    