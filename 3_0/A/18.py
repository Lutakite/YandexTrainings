k, n = map(int, input().split())
heapTime = list()
heapTime.append((0,0))
heapTupik = list()
heapTupik.append(0)

for i in range(1, k+1):
    heapTupik.append(i)

result = list()
error = False
for j in range(n):
    t1, t2 = map(int, input().split())
    #print(str(t1)+" "+str(t2))
    while len(heapTime) > 1 and t1 > heapTime[1][0]:
        #print("time magic")
        heapTupik.append(heapTime[1][1])
        i = len(heapTupik) - 1
        while i//2 > 0 and heapTupik[i // 2] > heapTime[1][1]:
            heapTupik[i//2], heapTupik[i] = heapTupik[i], heapTupik[i//2]
            i = i//2
            
        heapTime[1] = heapTime[len(heapTime)-1]    
        i = 1
        while i*2 < len(heapTime):
            if ((i*2+1 < len(heapTime) and heapTime[i*2][0] <= heapTime[i*2+1][0]) or i*2+1 == len(heapTime)) and heapTime[i*2][0] < heapTime[i][0]:
                heapTime[i*2], heapTime[i] = heapTime[i], heapTime[i*2]
                i = i*2
            elif i*2+1 < len(heapTime) and heapTime[i*2][0] > heapTime[i*2+1][0] and heapTime[i*2+1][0] < heapTime[i][0]: 
                heapTime[i*2+1], heapTime[i] = heapTime[i], heapTime[i*2+1]
                i = i*2+1
            else:
                break
        heapTime.pop()
    #print(heapTupik)
    #print(heapTime)
    if len(heapTupik) > 1:
        result.append(heapTupik[1])
        heapTime.append((t2, heapTupik[1]))
        #print(heapTime)
        i = len(heapTime) - 1
        #print(i//2)
        #print(heapTime[i // 2][0])
        #print(heapTime[1][0])
        while i//2 > 0 and heapTime[i // 2][0] > heapTime[i][0]:
            #print("here")
            heapTime[i//2], heapTime[i] = heapTime[i], heapTime[i//2]
            i = i//2
        #print(heapTime)    
        #print()    
        heapTupik[1] = heapTupik[len(heapTupik)-1]    
        i = 1
        while i*2 < len(heapTupik):
            if ((i*2+1 < len(heapTupik) and heapTupik[i*2] <= heapTupik[i*2+1]) or i*2+1 == len(heapTupik)) and heapTupik[i*2] < heapTupik[i]:
                heapTupik[i*2], heapTupik[i] = heapTupik[i], heapTupik[i*2]
                i = i*2
            elif i*2+1 < len(heapTupik) and heapTupik[i*2] > heapTupik[i*2+1] and heapTupik[i*2+1] < heapTupik[i]: 
                heapTupik[i*2+1], heapTupik[i] = heapTupik[i], heapTupik[i*2+1]
                i = i*2+1
            else:
                break
        heapTupik.pop()
        #print(heapTime)
    else:
        print("0 "+str(j+1))
        error = True
        break   
if not error:
    for i in result:
        print(i)