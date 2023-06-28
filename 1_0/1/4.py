a = int(input())
b = int(input())
c = int(input())

res = ""

if c < 0:
    res = "NO SOLUTION"
elif a == 0:
    if b < 0:
        res = "NO SOLUTION"
    elif b == c*c:
        res = "MANY SOLUTIONS"
    else:
        res = "NO SOLUTION"
else:
    d = c*c - b
    if d % a != 0:
        res = "NO SOLUTION"
    else:
        res = int(d / a)
    
print(res)
