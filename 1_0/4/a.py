n = int(input())

d = dict()
for _ in range(n):
    s = input().split()
    d[s[0]] = s[1]
    d[s[1]] = s[0]

s = input()
print(d[s])