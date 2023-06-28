s1 = input().split()
s2 = input().split()

#a = list(map(int, input().split()))
#print(*a, sep='-')

a = set()
for i in s1:
    a.add(i)

res = set()
for i in s2:
    if i in a:
        res.add(int(i))
        
print(*sorted(res), sep=' ')