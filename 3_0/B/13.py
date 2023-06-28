s = input().split()
stack = list()

for i in s:
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