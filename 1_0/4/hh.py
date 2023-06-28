g, S = map(int, input().split())

def gendict(word):
    res = dict()
    for w in word:
        res[w] = res.get(w,0) + 1
    return res

w = input()
wDict = gendict(w)
s = input()

result = 0
for i in range(S-g+1):
    sDict = gendict(s[i:i+g])
    if wDict == sDict:
        result += 1

print(result)
    