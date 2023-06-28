n = int(input())
from collections import deque
firstHalfQueue = deque()
secondHalfQueue = deque()

for _ in range(n):
    line = input()
    #print(line)
    if line == '-':
        print(firstHalfQueue.popleft())
        if len(firstHalfQueue) < len(secondHalfQueue) and len(secondHalfQueue) != 0:
            firstHalfQueue.append(secondHalfQueue.popleft())
    else:
        line = line.split()
        if line[0] == "+":
            secondHalfQueue.append(line[1])
            #print("first:")
            #print(len(firstHalfQueue))
            #print("second:")
            #print(len(secondHalfQueue))
            if len(firstHalfQueue) < len(secondHalfQueue) and len(secondHalfQueue) != 0:
                firstHalfQueue.append(secondHalfQueue.popleft())
        else:
            firstHalfQueue.append(line[1])
            if len(firstHalfQueue) > len(secondHalfQueue) + 1:
                secondHalfQueue.appendleft(firstHalfQueue.pop())
    #print("first:")
    #print(firstHalfQueue)
    #print("second:")
    #print(secondHalfQueue)


    