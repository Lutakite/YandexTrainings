import heapq
n, w = map(int, input().split())
tasks = list()
for i in range(n):
    a, t = map(int, input().split())
    tasks.append((a, a+t, str(i+1)))
tasks.sort()

workers = [[]]
workersTime = [(0,0)]
for task in tasks:
    #found = False
    t, i = workersTime[0]#heapq.heappop(workersTime)[0]
    #print(i)
    #for i in range(len(workersTime)):
    #    if workersTime[i] <= task[0]:
    #        found = True
    #        workers[i].append(task[2])
    #        workersTime[i] = task[1]
    #       break
    if t <= task[0]:
        workers[i].append(task[2])
        heapq.heappop(workersTime)[0]
        heapq.heappush(workersTime, (task[1], i))
    else:
        heapq.heappush(workersTime, (task[1], len(workers)))
        workers.append([task[2]])

print(len(workers))
for worker in workers:
    print(' '.join(worker), end = ' ')


