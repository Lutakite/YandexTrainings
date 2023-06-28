n, w = map(int, input().split())
tasks = list()
for i in range(n):
    a, t = map(int, input().split())
    tasks.append((a, a+t, i+1))
tasks.sort()

workers = []
for task in tasks:
    if not workers or workers[-1][-1] <= task[0]:
        workers.append((task[1], [task[2]]))
    else:
        for i, worker in enumerate(workers):
            if worker[0] <= task[0]:
                worker[0] = task[1]
                worker[1].append(task[2])
                break

print(len(workers))
for worker in workers:
    print(" ".join(map(str, worker[1])))


