a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

res = "NO"

if a <= d and b <= e:
    res = "YES"
elif a <= d and c <= e:
    res = "YES"
elif b <= d and a <= e:
    res = "YES"
elif b <= d and c <= e:
    res = "YES"
elif c <= d and a <= e:
    res = "YES"
elif c <= d and b <= e:
    res = "YES"
    
print(res)
