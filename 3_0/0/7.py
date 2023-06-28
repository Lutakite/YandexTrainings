x = input().split(":")
h1 = int(x[0])
m1 = int(x[1])
s1 = int(x[2])

x = input().split(":")
h2 = int(x[0])
m2 = int(x[1])
s2 = int(x[2])

x = input().split(":")
h3 = int(x[0])
m3 = int(x[1])
s3 = int(x[2])

if h3 < h1:
    h3 += 24
    
sec1 = h1*60*60 + m1*60 + s1
sec2 = h2*60*60 + m2*60 + s2
sec3 = h3*60*60 + m3*60 + s3

dif = sec3 - sec1
if dif%2 == 0:
    dif = dif // 2
else:
    dif = dif // 2 + 1

#print(dif)
#print(sec2)    
res = sec2 + dif
#print(res)

resS = res % 60
resM = (res // 60) % 60
resH = res // 3600

while resH >= 24:
    resH -= 24

def convert(x):
    result = ""
    if x < 10:
        result += "0"+str(x)
    else:
        result = str(x)
    return result
    
print(convert(resH)+":"+convert(resM)+":"+convert(resS))