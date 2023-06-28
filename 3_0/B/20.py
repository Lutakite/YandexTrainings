n = int(input())
n += 1
heap = [0] + list(map(int, input().split()))
#print(heap)
j = n // 2
while j > 0:
    i = j
    while i*2 < len(heap):
        if ((i*2+1 < len(heap) and heap[i*2] <= heap[i*2+1]) or i*2+1 == len(heap)) and heap[i*2] < heap[i]:
            heap[i*2], heap[i] = heap[i], heap[i*2]
            i = i*2
        elif i*2+1 < len(heap) and heap[i*2] > heap[i*2+1] and heap[i*2+1] < heap[i]: 
            heap[i*2+1], heap[i] = heap[i], heap[i*2+1]
            i = i*2+1
        else:
            break
    j -= 1
    #print(heap)

for j in range(1,n):
    print(heap[1], end = " ")
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