n = int(input())
s = input().split()

max = -1
#min = 1000000
for i in s:
    if int(i) > max:
        max = int(i)
    #if int(i) < min:
    #    min = int(i)
        
prevprev = int(s[0])
prev = int(s[1])
vas = -1
vinner = False
if prevprev == max:
    vinner = True
for i in range(2, len(s)):
    if vinner == True:
        if int(s[i]) < prev:
            if prev % 5 == 0 and prev % 2 != 0:
                if prev > vas:
                    vas = prev
    else:
        if prev == max:
            vinner = True
    
    prevprev = prev
    prev = int(s[i])

res = 0
if vas == -1:
    print(0)
else:
    for i in s:
        if int(i) > vas: 
            res += 1
    print(res + 1)
    