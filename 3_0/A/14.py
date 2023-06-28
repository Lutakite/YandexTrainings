s = list(map(int, input().split()))
n = s[0]
result = 0
min = 10000000000
stack = list()
stack.append((0,0))
s.append(0)
sresult = [0]*(n+2)
for i in range(1,n+2):
    res = 0
    if s[i] < min and s[i] != 0:
        min = s[i]
    while len(stack) > 0 and stack[-1][0] > s[i]:
        res = stack[-1][0]*(i-stack[-1][1])
        sresult[stack[-1][1]] = res
        if res > result:
            result = res
        stack.pop()
    if s[i] == 0 and len(stack) > 0:
        res = min * ((i-stack[0][1])-1)
        if res > result:
            result = res
        min = 10000000000
        stack = list()
    if len(stack) == 0 or (len(stack) > 0 and stack[-1][0] != s[i]):
        stack.append((s[i], i))

#print(s)
s.reverse()
s.pop()
s.append(0)
#print(s)        
stack = list()
stack.append((0,0))
sresult2 = [0]*(n+2)

for i in range(1,n+2):
    res = 0
    if s[i] < min and s[i] != 0:
        min = s[i]
    while len(stack) > 0 and stack[-1][0] > s[i]:
        res = stack[-1][0]*(i-stack[-1][1])
        sresult2[stack[-1][1]] = res - stack[-1][0]
        #print(sresult2[stack[-1][1]] + sresult2[n+1-stack[-1][1]] - stack[-1][0])
        if res > result:
            result = res
        stack.pop()
    if s[i] == 0 and len(stack) > 0:
        res = min * ((i-stack[0][1])-1)
        if res > result:
            result = res
        min = 10000000000
        stack = list()
    if len(stack) == 0 or (len(stack) > 0 and stack[-1][0] != s[i]):
        stack.append((s[i], i))

for i in range(1, len(sresult)-1):
    #print(i)
    #print(n+1-i)
    res = sresult[i] + sresult2[n+1-i]
    if res > result:
        result = res
print(result)
    