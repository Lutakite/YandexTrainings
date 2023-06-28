n, m = map(int, input().split())
segments = list()
for _ in range(n):
    b, c = map(int, input().split())
    if b > c:
        b, c = c, b
    segments.append((b, '1'))
    segments.append((c+1, '-1'))

ms = list(map(int,input().split()))
for i in ms:
    segments.append((i, '10'))
segments.sort()

res = 0
#print(segments)
result = dict()
for s in segments:
    if s[1] == '10':
        result[s[0]] = res
    else:
        res += int(s[1])
        
for i in ms:
    print(result[i], end=" ")
    