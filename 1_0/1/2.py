a = int(input())
b = int(input())
c = int(input())
res = "YES"
if (a + b <= c):
    res = "NO"
if (a + c <= b):
    res = "NO"
if (b + c <= a):
    res = "NO"
print(res)
