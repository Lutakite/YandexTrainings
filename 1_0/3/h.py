n = int(input())
setx = set()
for i in range(n):
    x = input().split()[0]
    setx.add(x)
print(len(setx))