from collections import deque
import heapq
n, k, p = map(int, input().split())
play = list()
cars = dict()
for i in range(p):
    car = int(input())
    play.append(car)
    if car not in cars:
        cars[car] = deque()
    cars[car].append(i)

def removemax(heap, carsplaynextind):
    #print(heap[1])
    heap[1] = heap[len(heap)-1]
    i = 1
    carsplaynextind[heap[1][1]] = i
    while i*2 < len(heap):
        if ((i*2+1 < len(heap) and heap[i*2][0] >= heap[i*2+1][0]) or i*2+1 == len(heap)) and heap[i*2][0] > heap[i][0]:
            heap[i*2], heap[i] = heap[i], heap[i*2]
            carsplaynextind[heap[i*2][1]] = i*2
            carsplaynextind[heap[i][1]] = i
            i = i*2
        elif i*2+1 < len(heap) and heap[i*2][0] < heap[i*2+1][0] and heap[i*2+1][0] > heap[i][0]: 
            heap[i*2+1], heap[i] = heap[i], heap[i*2+1]
            carsplaynextind[heap[i*2+1][1]] = i*2+1
            carsplaynextind[heap[i][1]] = i
            i = i*2+1
        else:
            break
    heap.pop()
    return heap, carsplaynextind
    
def add2maxheap(heap, x, car, carsplaynextind):
    heap.append((x, car))
    i = len(heap) - 1
    carsplaynextind[car] = i
    while i//2 > 0 and heap[i // 2][0] < x:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        carsplaynextind[heap[i//2][1]] = i//2
        carsplaynextind[heap[i][1]] = i
        i = i//2
    return heap, carsplaynextind
    
def changeheap(heap, i, x, carsplaynextind):
    #print(heap[i])
    #heap[i][0] = x
    heap[i] = (x, heap[i][1])
    carsplaynextind[heap[i][1]] = i
    while i//2 > 0 and heap[i // 2][0] < x:
        heap[i//2], heap[i] = heap[i], heap[i//2]
        carsplaynextind[heap[i//2][1]] = i//2
        carsplaynextind[heap[i][1]] = i
        i = i//2
    return heap, carsplaynextind
      
result = 0
empty = k
carsplay = set()
carsplaynext = list()
carsplaynext.append((0,0))
carsplaynextind = dict()

for i in range(p):
    car = play[i]
    #print("шаг "+str(i)+": wants to play with car number "+str(car))
    if car not in carsplay:
        result += 1
        if empty > 0:
            empty -= 1
        else:
            maxcar = carsplaynext[1][1]
            carsplay.remove(maxcar)
            removemax(carsplaynext,carsplaynextind)
            #print("removing car "+str(maxcar))
        carsplay.add(car)
        pos = p+1
        if len(cars[car])>1:
            pos = cars[car][1]
        #print(carsplaynext)
        #print
        add2maxheap(carsplaynext,pos,car,carsplaynextind)
    else:
        nextplay = p+1
        if len(cars[car]) > 1:
            nextplay = cars[car][1]
        changeheap(carsplaynext, carsplaynextind[car], nextplay, carsplaynextind)
        #нужно обновить хип
    cars[car].popleft()
    #print(carsplaynext)
    
    #for j in range(1,len(carsplaynext)):
    #    if carsplaynextind[carsplaynext[j][1]] != j:
    #        print("ahtung")
    #        print(carsplaynext[j][1])
    #        print(carsplaynextind[carsplaynext[j][1]])
    #        print(j)
    #        print(carsplaynext)
    #        print(carsplaynextind)

print(result)