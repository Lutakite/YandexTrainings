n = int(input())
for _ in range(n):
    s = list(map(float, input().split()))
    k = int(s[0])
    ssort = sorted(s[1:])
    #print(ssort)
    stack = list()
    ind = 0
    for i in range(1, k+1):
        #print("i="+str(i)+"; s[i]="+str(s[i])+"; ind="+str(ind)+"; ssort[ind]="+str(ssort[ind]))
        if s[i] == ssort[ind]:
            #last = s[i]
            ind += 1
            while len(stack) > 0 and stack[-1] == ssort[ind]:
                ind += 1
                stack.pop()
        else:
            stack.append(s[i])
        #print(stack)
    if len(stack) == 0:
        print(1)
    else:
        print(0)