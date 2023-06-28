from sys import stdin

d = dict()
res = ""
for line in stdin:
    words = line.split()
    for word in words:
        res += str(d.get(word, 0)) + " "
        d[word] = d.get(word,0) + 1
print(res[:len(res)-1])