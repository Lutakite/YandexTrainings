n = int(input())
heap = list()
heap.append(0)

for _ in range(n):
    s = input()
    if s=="1":
        print(heap[1])
        heap[1] = heap[len(heap)-1]
        i = 1
        while i*2 < len(heap):
            if ((i*2+1 < len(heap) and heap[i*2] >= heap[i*2+1]) or i*2+1 == len(heap)) and heap[i*2] > heap[i]:
                heap[i*2], heap[i] = heap[i], heap[i*2]
                i = i*2
            elif i*2+1 < len(heap) and heap[i*2] < heap[i*2+1] and heap[i*2+1] > heap[i]: 
                heap[i*2+1], heap[i] = heap[i], heap[i*2+1]
                i = i*2+1
            else:
                break
        heap.pop()
    else:
        x = int(s.split()[1])
        heap.append(x)
        i = len(heap) - 1
        while i//2 > 0 and heap[i // 2] < x:
            heap[i//2], heap[i] = heap[i], heap[i//2]
            i = i//2