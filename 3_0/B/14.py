n = int(input())
s = list(map(int, input().split()))

stack = list()
last = 0
for i in range(n):
    #print("i="+str(i)+"; s[i]="+str(s[i])+"; last="+str(last))
    if s[i] == last + 1:
        last = s[i]
        while len(stack) > 0 and stack[-1] == last + 1:
            last += 1
            stack.pop()
    else:
        stack.append(s[i])
    #print(stack)
if len(stack) == 0:
    print("YES")
else:
    print("NO")