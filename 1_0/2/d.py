s = input().split()

result = 0
if len(s) > 2:
    prevprev = int(s[0])
    prev = int(s[1])
    for i in range(2,len(s)):
        si = int(s[i])
        if prev > prevprev and prev > si:
            result += 1
        prevprev = prev
        prev = si
        
print(result)
