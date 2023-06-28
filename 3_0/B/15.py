n = int(input())
s = list(map(int, input().split()))

result = s
stack = list()
for i in range(n):
    #print("i="+str(i)+"; s[i]="+str(s[i]))
    while len(stack) > 0 and stack[-1][0] > s[i]:
        result[stack[-1][1]] = i
        stack.pop()
    stack.append((s[i], i))
    #print(stack)

for i in range(len(stack)):
    result[stack[i][1]] = -1
for r in result:
    print(r, end=" ")
    