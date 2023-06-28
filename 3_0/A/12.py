def getpriority(symbol):
    if symbol == "+" or symbol == "-":
        return 0
    else:
        return 1
        
def checkskobki(skobki):
    stack = list()
    result = True
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        elif i == ")":
            if len(stack) < 1:
                result = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                result = False
                break
        elif i == "]":
            if len(stack) < 1:
                result = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                result = False
                break
        elif i == "}":
            if len(stack) < 1:
                result = False
                break
            if stack[-1] == "{":
                stack.pop()
            else:
                result = False
                break

    if len(stack) > 0:
        result = False
    return result
s = input()

skobki = ""

badnum = False

#print(s)
for i in range(len(s)):
    symbol = s[i]
    if symbol == "(" or symbol == ")":
        skobki += symbol
    if symbol >= "0" and symbol <= "9":
        #print("checking")
        #print(symbol)
        #print(i)
        j = i - 1
        if s[j] == " ":
            #print("checking2")
            while j > 0 and s[j] == " ":
                j -= 1
            #if j >= 0: print(s[j])
            if j >= 0 and s[j] >= "0" and s[j] <= "9":
                badnum = True
    if symbol not in "01234567890 +-*()":
        #print(symbol)
        badnum = True

if s[len(s)-1] == "+" or s[len(s)-1] == "-" or s[len(s)-1] == "*":
    badnum = True
if badnum==True or checkskobki(skobki)==False:
    print("WRONG")
else:
    #print(s)
    s = s.replace(" ", "")
    i = 0
    s += "E"
    error = False
    while True:
        if i == len(s):
            break
        if s[i] == "*":
            if (i > 0 and (s[i-1] < "0" or s[i-1] > "9") and s[i-1] != ")") or i==0:
                error = True
        if (s[i] == "-" or s[i] == "+"):
            if i > 0 and (s[i-1] < "0" or s[i-1] > "9") and s[i-1] != ")":
                j = i+1
                while s[j] >="0" and s[j] <= "9":
                    j += 1
                #print("j="+str(j)+";s[j]="+s[j])
                #print(s)
                #print(s[:i])
                #print(s[i:j])
                #print(s[j:])
                s = s[:i]+"(0"+s[i:j]+")"+s[j:]
                #print(s)
            elif i == 0:
                j = i+1
                while s[j] >="0" and s[j] <= "9":
                    j += 1
                #print("j="+str(j))
                s = s[:i]+"(0"+s[i:j]+")"+s[j:]
                #print(s)
        i += 1
    if error:
        print("WRONG")
        
    else:
        #print(s)
        postfix = list()
        stack = list()

        result = list()
        prev = ""
        probel = False
        for symbol in s:
            #print("symbol="+symbol)
            if symbol == "E":
                if prev != "":
                    result.append(prev)
                prev = ""
            if symbol == " ":
                if prev != "":
                    result.append(prev)
                prev = ""
            elif symbol == "+" or symbol == "-" or symbol == "*":
                if prev != "":
                    result.append(prev)
                prev = ""
                while len(postfix) > 0 and postfix[-1]!="(" and getpriority(postfix[-1]) >= getpriority(symbol):
                    result.append(postfix[-1])
                    postfix.pop()
                postfix.append(symbol)
                prev = ""
            elif symbol == "(":
                if prev != "":
                    result.append(prev)
                prev = ""
                postfix.append(symbol)
                prev = ""
            elif symbol == ")":
                #print(postfix)
                if prev != "":
                    result.append(prev)
                prev = ""
                while len(postfix) > 0 and postfix[-1]!="(":
                    result.append(postfix[-1])
                    postfix.pop()
                if len(postfix) > 0 and postfix[-1]=="(":
                    postfix.pop()
                prev = ""
                #print("ok")
                #print(postfix)
            else:
                prev += symbol
        while len(postfix) > 0:
            result.append(postfix[-1])
            postfix.pop()
        #print(result)

        for i in result:
            if i != "+" and i != "-" and i != "*":
                stack.append(int(i))
            else:
                if i == "+":
                    stack[-2] += stack[-1]
                    stack.pop()
                elif i == "-":
                    stack[-2] -= stack[-1]
                    stack.pop()
                else:
                    stack[-2] *= stack[-1]
                    stack.pop()

        print(stack[0])