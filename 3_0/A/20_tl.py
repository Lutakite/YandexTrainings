from collections import deque
n, k, p = map(int, input().split())
play = list()
cars = dict()
for i in range(p):
    car = int(input())
    play.append(car)
    if car not in cars:
        cars[car] = deque()
    cars[car].append(i)
    
#for car in cars:
#    heapq.heapify(cars[car])

result = 0
empty = k
carsplay = set()
for i in range(p):
    car = play[i]
    #print("wants to play with car number "+str(car))
    if car not in carsplay:
        result += 1
        if empty > 0:
            empty -= 1
        else:
            max = 0
            maxcar = 0
            for c in carsplay:
                #if len(cars[c]) == 0:
                if c not in cars:
                    maxcar = c
                    break
                if cars[c][0] > max:
                    max = cars[c][0]
                    maxcar = c
            #print("remove car number "+str(maxcar))
            carsplay.remove(maxcar)        
        carsplay.add(car)
    if len(cars[car]) == 1:
        del cars[car]
    else:
        cars[car].popleft()
    #heapq.heappop(cars[car])
print(result)