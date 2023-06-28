a = int(input())
b = int(input())
n = int(input())
m = int(input())

max = 0
min = 0

max1 = a*(n+1) + n
min1 = a*(n-1) + n

max2 = b*(m+1) + m
min2 = b*(m-1) + m

if max1 >= max2:
    max = max2
else:
    max = max1
if min1 >= min2:
    min = min1
else:
    min = min2
    
if min <= max:
    print(str(min)+" "+str(max))
else:
    print(-1)
