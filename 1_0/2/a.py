str = input().split()

result = "YES"
prev = int(str[0])
for i in range(1,len(str)):
    s = int(str[i])
    if s <= prev:
        result = "NO"
        break
    prev = s
    
print(result)
