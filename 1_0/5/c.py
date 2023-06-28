n = int(input())

def countprefixsumsplus(mass, length, positive):
    result = [0] * (length+1)
    if positive == True:
        for i in range(length-1):
            if mass[i+1] >= 0:
                result[i+1] = result[i] + mass[i+1]
            else:
                result[i+1] = result[i]
    else:
        for i in range(length,0,-1):
            if mass[i-1] <= 0:
                result[i-1] = result[i] - mass[i-1]
            else:
                result[i-1] = result[i]       
    return result
    
def convert2delthas(mass):
    result = [0] * len(mass)
    for i in range(1,len(mass)):
        result[i] = mass[i] - mass[i-1]
    return result

mountains = [0] * (n)
for i in range(0, n):
    mountains[i] = int(input().split()[1])
    
#print(mountains)
mountains = convert2delthas(mountains)
#print(mountains)
#print()

mountainsFromL2R = countprefixsumsplus(mountains, len(mountains), True)
mountainsFromR2L = countprefixsumsplus(mountains, len(mountains), False)

#print(mountainsFromL2R)
#print(mountainsFromR2L)
m = int(input())

for _ in range(m):
    l, r = map(int, input().split())
    #print(l,r)
    if l<=r:
        print(str(mountainsFromL2R[r-1]-mountainsFromL2R[l-1]))
    else:
        print(str(mountainsFromR2L[r]-mountainsFromR2L[l]))
        