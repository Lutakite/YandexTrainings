def getpriority(symbol):
    if symbol == "^" or symbol == "|":
        return 0
    elif symbol == "&":
        return 1
    else:
        return 2

s = input()

postfix = list()
stack = list()

result = list()
for symbol in s:
    if symbol == "&" or symbol == "!" or symbol == "|" or symbol == "^":
        while len(postfix) > 0 and postfix[-1]!="(" and getpriority(postfix[-1]) >= getpriority(symbol):
            result.append(postfix[-1])
            postfix.pop()
        postfix.append(symbol)
    elif symbol == "(":
        postfix.append(symbol)
    elif symbol == ")":
        while len(postfix) > 0 and postfix[-1]!="(":
            result.append(postfix[-1])
            postfix.pop()
        if len(postfix) > 0 and postfix[-1]=="(":
            postfix.pop()
    else:
        result += symbol
while len(postfix) > 0:
    result.append(postfix[-1])
    postfix.pop()
#print(result)

for i in result:
    if i == "0" or i == "1":
        stack.append(int(i))
    else:
        if i == "&":
            stack[-2] &= stack[-1]
            stack.pop()
        elif i == "|":
            stack[-2] |= stack[-1]
            stack.pop()
        elif i == "^":
            stack[-2] ^= stack[-1]
            stack.pop()
        else:
            if stack[-1] == 1:
                stack[-1] = 0
            else:
                stack[-1] = 1
    #print(i)
    #print(stack)
print(stack[0])