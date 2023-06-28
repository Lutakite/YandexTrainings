n = int(input())

dictionary = dict()
for _ in range(n):
    w = input()
    word = w.lower()
    if word not in dictionary:
        dictionary[word] = list()
    dictionary[word].append(w)

result = 0
s = input().split()
for w in s:
    word = w.lower()
    if word in dictionary:
        if w not in dictionary[word]:
            result += 1
    else:
        c = 0
        for letter in w:
            if letter >= 'A' and letter <= 'Z':
                c += 1
        if c != 1:
            result += 1

print(result)
            