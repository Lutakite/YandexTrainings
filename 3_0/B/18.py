from sys import stdin

deque = [0]*100
head = 0
tail = 0
#print(deque)
for line in stdin:
    #print("line="+line)
    line = line.strip()
    if line == "exit":
        print("bye")
        break
    elif line == "clear":
        head = 0
        tail = 0
        print("ok")
    elif line == "size":
        print(tail-head)
    elif line == "front":
        if tail-head == 0:
            print("error")
        else:
            print(deque[(head+1)%100])
    elif line == "back":
        if tail-head == 0:
            print("error")
        else:
            print(deque[tail%100])
    elif line == "pop_front":
        if tail-head == 0:
            print("error")
        else:
            print(deque[(head+1)%100])
            head = head+1
    elif line == "pop_back":
        if tail-head == 0:
            print("error")
        else:
            print(deque[tail%100])
            tail = tail-1
    else:
        line, n = line.split()
        if line == "push_front":
            deque[head%100] = n
            head = head-1
            print("ok")
        elif line == "push_back":
            tail = tail+1
            deque[tail%100] = n
            print("ok")
    #print(line)
    #print(deque)
    #print("head="+str(head))
    #print("tail="+str(tail))
        


    