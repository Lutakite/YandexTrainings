s = input().split()
n = int(s[0])
m = int(s[1])

bothset = set()
annset = set()
borisset = set()
for i in range(n):
    annset.add(int(input()))
for j in range(m):
    borisset.add(int(input()))

bothset = annset & borisset
annset -= bothset
borisset -= bothset

print(len(bothset))
print(*sorted(bothset), sep=' ')
print(len(annset))
print(*sorted(annset), sep=' ')
print(len(borisset))
print(*sorted(borisset), sep=' ')
