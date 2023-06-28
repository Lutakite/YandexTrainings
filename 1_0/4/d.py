n = int(input())
c = input().split()

resources = dict()
for i in range(1,n+1):
    resources[i] = int(c[i-1])

k = int(input())
p = input().split()

for pi in p:
    resources[int(pi)] -= 1
    
for i in range(1,n+1):
    if resources[i] < 0:
        print("YES")
    else:
        print("NO")