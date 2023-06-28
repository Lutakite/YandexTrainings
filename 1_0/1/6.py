s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

min = -1
v = ""
res = 1
#1
if a >= c:
    v = str(a) + " " + str(b + d)
    min = a * (b + d)
else: 
    v = str(c) + " " + str(b + d)
    min = c * (b + d)
    
#2    
if a >= d: 
    m = a * (b + c)
    if m < min:
        min = m
        v = str(a) + " " + str(b + c)
else:
    m = d * (b + c)
    if m < min:
        min = m
        v = str(d) + " " + str(b + c)

#3    
if b >= c: 
    m = b * (a + d)
    if m < min:
        min = m
        v = str(b) + " " + str(a + d)
else:
    m = c * (a + d)
    if m < min:
        min = m
        v = str(c) + " " + str(a + d)
        
#4    
if b >= d: 
    m = b * (a + c)
    if m < min:
        min = m
        v = str(b) + " " + str(a + c)
else:
    m = d * (a + c)
    if m < min:
        min = m
        v = str(d) + " " + str(a + c)
        
print(v)
