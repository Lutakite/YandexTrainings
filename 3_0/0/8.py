n = int(input())
minx = 100000000000
miny = 100000000000
maxx = -100000000000
maxy = -100000000000
for _ in range(n):
    x, y = map(int, input().split())
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y
print(str(minx)+" "+str(miny)+" "+str(maxx)+" "+str(maxy))
    