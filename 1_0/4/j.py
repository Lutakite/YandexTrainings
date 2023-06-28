from sys import stdin
lines = stdin.readlines()
line = lines[0].split()
n = int(line[0])
reg = False
if line[1] == "yes":
    reg = True
numbegin = False
if line[2] == "yes":
    numbegin = True

def checkword(word, numbegin):
    if numbegin == False and word[0] >= '0' and word[0] <= '9':
        return False
    if word in keywords:
        return False
    for letter in word:
        if (letter >= 'A' and letter <= 'Z') or (letter >= 'a' and letter <= 'z') or letter == '_':
            return True
    return False
    
keywords = set()

ids = dict()
pos = 0
for i in range(1,n+1):
    line = lines[i].split('\n')[0]
    if reg:
        keywords.add(line)
    else:
        keywords.add(line.lower())

for i in range(n+1,len(lines)):
    line = lines[i]
    
    word = ""
    for l in line:
        if (l >= 'a' and l <= 'z') or (l >= 'A' and l <= 'Z') or l == '_' or (l >= '0' and l <= '9'):
            word += l
        else: #word кончился
            if reg == False:
                word = word.lower()
            if word != "":
                if word in ids:
                    ids[word][0] += 1
                elif checkword(word, numbegin):
                    ids[word] = [1, pos]
                    pos += 1
                word = ""
   
resid = ""
residpos = -1
resmax = 0 
for id in ids:
    if ids[id][0] > resmax:
        resmax = ids[id][0]
        resid = id
        respos = ids[id][1]
    elif ids[id][0] == resmax:
        if respos > 0 and respos > ids[id][1]:
            respos = ids[id][1]
            resid = id
            
print(resid)