directions = [-1] * (1 + ord('Z'))
counts = []
count = []
chars = ['N', 'S', 'W', 'E', 'U', 'D']
for i in range(len(chars)):
    directions[ord(chars[i])] = i
for i in range(len(chars)):
    counts.append([0] * len(chars))
for i in range(len(chars)):
    strr = input()
    for cc in strr:
        counts[i][directions[ord(cc)]] += 1
direction_result, parametr_result = map(str, input().split())
parametr_result = int(parametr_result)
for i in range(1 + parametr_result):
    count.append([1] * len(chars))
for par in range(2, parametr_result + 1):
    for parentDir in range(len(chars)):
        for chilDir in range(len(chars)):
            res = count[par - 1][chilDir] * counts[parentDir][chilDir]
            count[par][parentDir] += res
print(count[parametr_result][directions[ord(direction_result)]])
print(counts)
print(directions)