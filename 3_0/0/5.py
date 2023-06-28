n = int(input())

letters = list()
result = 0
for i in range(n):
    c = int(input())
    letters.append(c)
    if i > 0:
        result += min(letters[i-1], c)
print(result)