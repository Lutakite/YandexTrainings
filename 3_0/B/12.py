try:
    s = input()
    
except EOFError as e:
    s = ""
    
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
if result == True:
    print("yes")
else:
    print("no")
