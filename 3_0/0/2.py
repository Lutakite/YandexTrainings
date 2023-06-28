k = int(input())
s = input()

n = len(s)

result = 0
l = 0
r = 0
#resultL = 0
#resultR = 0
#resultLen = 0
#print(s)
max = 0
countLetters = dict()
while r < n and l < n:
    #print("l="+str(l)+"; r="+str(r))
    countLetters[s[r]] = countLetters.get(s[r],0) + 1
    if r - l + 1 >= countLetters[s[l]] + k:
        if countLetters[s[l]] + k > max:
            max = countLetters[s[l]] + k
        if not (r < n-1 and s[r+1] == s[l]):
            countLetters[s[l]] -= 1
            l += 1
    r += 1
        
    
print(str(max))
    