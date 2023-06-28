n = int(input())
classes = list(map(int, input().split()))
m = int(input())

conditioners = dict()
watts = list()
for i in range(m):
    b, c = list(map(int, input().split()))
    #print(b,c)
    if c < conditioners.get(b, 1002):
        conditioners[b] = c
    if b not in watts:
        watts.append(b)
    #print(conditioners)
        
watts = sorted(watts)
#print(watts)
#print(conditioners)
min = 1002
result = 0
classes = sorted(classes)

right = len(watts) - 1
for i in range(n-1,-1,-1):
    #print("i="+str(i))
    #print(right)
    #print(watts[right])
    #print(classes[i])
    while right >= 0 and watts[right] >= classes[i]:
        if conditioners[watts[right]] < min:
            min = conditioners[watts[right]]
        right -= 1
    #print(min)
    result += min
print(result)