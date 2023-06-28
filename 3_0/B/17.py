a = list(map(int, input().split()))
b = list(map(int, input().split()))
ahead = 0
bhead = 0
i = 0
def checkbigger(x, y):
    if x==0 and y==9:
        return True
    if x==9 and y==0:
        return False
    return x > y
while i < 1000000:
    i += 1
    if checkbigger(a[ahead], b[bhead]):        
        a.append(a[ahead])
        a.append(b[bhead])
    else:        
        b.append(a[ahead])
        b.append(b[bhead])
        
    ahead += 1
    bhead += 1
    if len(a) - ahead == 0:
        result = "second "+str(i)
        break
    if len(b) - bhead == 0:
        result = "first "+str(i)
        break
    
if i == 1000000:
    print("botva")
else:
    print(result)