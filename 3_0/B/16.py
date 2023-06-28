from sys import stdin

queue = list()
head = 0
for line in stdin:
    #print("line="+line)
    line = line.strip()
    if line == "exit":
        print("bye")
        break
    elif line == "clear":
        queue = list()
        head = 0
        print("ok")
    elif line == "size":
        print(len(queue)-head)
    elif line == "front":
        if len(queue)-head == 0:
            print("error")
        else:
            print(queue[head])
    elif line == "pop":
        if len(queue)-head == 0:
            print("error")
        else:
            print(queue[head])
            head += 1
    else:
        #print(line)
        line, n = line.split()
        queue.append(n)
        print("ok")
        


    