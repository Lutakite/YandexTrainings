from sys import stdin

res = set()
for line in stdin:
    words = line.split()
    for word in words:
        res.add(word)

print(len(res))