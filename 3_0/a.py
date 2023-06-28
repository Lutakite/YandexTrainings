n = int(input())
ns = list(map(int, input().split()))

prev = ns[0]
result = ns[n-1] - ns[0]
for i in range(1,n):
    if ns[i] >= prev:
        prev = ns[i]
    else:
        result = -1
        break
print(result)