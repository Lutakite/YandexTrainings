from sys import stdin

stack = list()
for line in stdin:
    #print("line="+line)
    line = line.strip()
    if line == "exit":
        print("bye")
        break
    elif line == "clear":
        stack = list()
        print("ok")
    elif line == "size":
        print(len(stack))
    elif line == "back":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[len(stack)-1])
    elif line == "pop":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[len(stack)-1])
            stack.pop()
    else:
        #print(line)
        line, n = line.split()
        stack.append(n)
        print("ok")
        


    