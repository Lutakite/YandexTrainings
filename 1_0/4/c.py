from sys import stdin

d = dict()
max = 0
for line in stdin:
    words = line.split()
    for word in words:
        d[word] = d.get(word,0) + 1
        if d[word] > max:
            max = d[word]
s = set()
for word, count in d.items():
    if count == max:
        s.add(word)
        
print(sorted(s)[0])