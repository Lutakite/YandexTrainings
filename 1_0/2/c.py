n = int(input())
m = input().split()
x = int(input())

deltha = 10000
res = 0
for i in m:
    i = int(i)
    d = abs(x-i)
    if d < deltha:
        deltha = d
        res = i
        
print(res)
