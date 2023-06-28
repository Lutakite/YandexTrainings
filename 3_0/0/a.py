from sys import stdin

d = dict()
max = 0
#res = ""
for line in stdin:
    words = line.split()
    for word in words:
        for symbol in word:
            #res += str(d.get(symbol, 0)) + " "
            d[symbol] = d.get(symbol,0) + 1
            if d[symbol] > max:
                max = d[symbol]
#print(res[:len(res)-1])
symbols = sorted(d)
for i in range(max, 0, -1):
    #print(i)
    for s in symbols:
        #print(d[s])
        if d[s] < i:
            print(" ",end="")
        else:
            print("#",end="")
    print("",end="\n")
for s in symbols:
    print(s,end="")
