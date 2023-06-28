g, S = map(int, input().split())

def gendict(word):
    res = dict()
    for w in word:
        res[w] = res.get(w,0) + 1
    return res

w = input()
wDict = gendict(w)
l = len(wDict)

s = input()

result = 0

sDict = gendict(s[0:g])
letters_ok = 0

for el in sDict:
    if sDict[el] == wDict.get(el,0):
        letters_ok += 1
if letters_ok == l:
    result += 1
#if wDict == sDict:
#    result += 1

for i in range(0,S-g):
    if sDict.get(s[i]) == 1:
        sDict.pop(s[i])
        if wDict.get(s[i],0) == 1:
            letters_ok -= 1
    else:
        if wDict.get(s[i],0) == sDict[s[i]]:
            letters_ok -= 1
        sDict[s[i]] = sDict[s[i]] - 1
        if wDict.get(s[i],0) == sDict[s[i]]:
            letters_ok += 1
            
    if wDict.get(s[i+g],0) == sDict.get(s[i+g],-1):
            letters_ok -= 1
    sDict[s[i+g]] = sDict.get(s[i+g],0) + 1
    if sDict[s[i+g]] == wDict.get(s[i+g],0):
        letters_ok += 1
       
    if letters_ok == l:
        result += 1

print(result)
    