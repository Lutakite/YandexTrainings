n = int(input())
s = input().split()

def checkreverse(s):
    l = len(s)//2
    for i in range(0,l):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
    
for i in range(0, n):
    if checkreverse(s[i:]) == True:
        print(i)
        if i != 0:
            print(' '.join(reversed(s[0:i])))
        break
        