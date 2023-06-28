s = input()

tag = ""
close = False

prevSymbol = ""
stackTagsOpening = list()
stackTagsClosing = list()
possibleErrors = list()
istart = 0

for i in range(len(s)):
    symbol = s[i]
    tag += symbol
    if symbol == '<':
        istart = i
    elif symbol == '/':
        close = True
        if prevSymbol != '<':
            possibleErrors.append((istart, i))
    elif symbol == '>':
        if close:
            stackTagsClosing.append((tag, istart, i))
        else:
            stackTagsOpening.append((tag, istart, i))
        tag = ""
        close = False
    prevSymbol = symbol

print(stackTagsOpening)
print(stackTagsClosing)
result = ""

if len(stackTagsClosing) < len(stackTagsOpening): #значит где-то потерян слэш
    while len(stackTagsClosing)>0 and stackTagsOpening[-1][0] == stackTagsClosing[-1][0][0]+stackTagsClosing[-1][0][2:]:
        stackTagsClosing.pop()
        stackTagsOpening.pop()
    if len(stackTagsClosing) == len(stackTagsOpening) - 2: #значит просто слэша не хватает
        result = s[:stackTagsOpening[-1][1]+1] + '/' + s[stackTagsOpening[-1][1]+2:]
    if len(stackTagsClosing) == len(stackTagsOpening) - 1: #- надо поделить тег на 2
        prev = ''
        for i in range(len(stackTagsOpening[-1][0])):
            if stackTagsOpening[-1][0][i] == '<' and i > 0 and prev != '>':
                result = s[:stackTagsOpening[-1][1]+i-1] + '>' + s[stackTagsOpening[-1][1]+i:]
                break
    if len(stackTagsClosing) == len(stackTagsOpening) - 3:# - 3 - первый закрывающий > это слеш
        result = s[:stackTagsOpening[-2][1]+1] + '/' + s[stackTagsOpening[-2][1]+2:]
elif len(stackTagsClosing) > len(stackTagsOpening): #значит где-то лишний слэш
    while len(stackTagsOpening)>0 and stackTagsOpening[-1][0] == stackTagsClosing[-1][0][0]+stackTagsClosing[-1][0][2:]:
        stackTagsClosing.pop()
        stackTagsOpening.pop()
    if len(stackTagsClosing) == len(stackTagsOpening) + 1: #- надо поделить тег на 2
        prev = ''
        for i in range(len(stackTagsClosing[-1][0])):
            if stackTagsClosing[-1][0][i] == '<' and i > 0 and prev != '>':
                #print(i)
                result = s[:stackTagsClosing[-1][1]-1] + '>' + s[stackTagsClosing[-1][1]:]
                break
else:#тут ошибка в букве
    while len(stackTagsOpening)>0 and stackTagsOpening[-1][0] == stackTagsClosing[-1][0][0]+stackTagsClosing[-1][0][2:]:
        stackTagsClosing.pop()
        stackTagsOpening.pop()
    result = s[:stackTagsClosing[-1][1]+2] + s[stackTagsOpening[-1][1]+1:stackTagsOpening[-1][1]+len(stackTagsOpening[-1][0])] + s[stackTagsClosing[-1][1]+len(stackTagsClosing[-1][0]):]    
print(result)