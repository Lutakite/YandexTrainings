n = int(input())
max = n-1

res = set()

for i in range(n):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    if a >= 0 and b >= 0:
        if a+b == max:
            res.add((a,b))

print(len(res))