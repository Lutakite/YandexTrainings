newtel = input().replace(')','').replace('(','').replace('-','')

if len(newtel) == 7:
    newtel = "8495" + newtel

if len(newtel) == 12:
    newtel = "8" + newtel[2:]

n = 3
i = 0
while i < 3:
    tel = input().replace(')','').replace('(','').replace('-','')
    
    if len(tel) == 7:
        tel = "8495" + tel

    if len(tel) == 12:
        tel = "8" + tel[2:]
    
    res = "NO"
    if (tel == newtel):
        res = "YES"
    print(res)
    i += 1
    