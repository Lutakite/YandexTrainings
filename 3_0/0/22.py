k = int(input())
s = input()

n = len(s)

result = 0
l = 0
r = 0
max = 0
countLetters = dict()
while r < n and l < n:
    #print("l="+str(l)+"; r="+str(r))
    countLetters[s[r]] = countLetters.get(s[r],0) + 1
    if r - l + 1 >= countLetters[s[l]] + k:
        rr = r + 1
        count = countLetters[s[l]] + k
        while rr < n and s[rr] == s[l]:
            #print("here")
            count += 1
            rr += 1 
        if count > max:
            max = count
            #rr = r + 1
            #while rr < n and s[rr] == s[l]:
            #    max += 1
            #    rr += 1       
        countLetters[s[l]] -= 1
        l += 1
        countLetters[s[r]] -= 1
        r -= 1
        #print(count)
        #print()
    r += 1
while l < n: 
    #print("l="+str(l)+"; r="+str(r))
    if countLetters[s[l]] + k > max:
        max = countLetters[s[l]] + k
    #print(countLetters[s[l]] + k)
    #print()
    countLetters[s[l]] -= 1
    l += 1
        
    
print(str(max))
    