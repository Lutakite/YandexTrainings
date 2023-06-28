t, d, n = map(int,input().split())

def plusd(rect, d):
    xmin, xmax, ymin, ymax = rect
    return [xmin-d, xmax+d, ymin-d, ymax+d]
    
def intersect(rect1, rect2):
    xmin1, xmax1, ymin1, ymax1 = rect1
    xmin2, xmax2, ymin2, ymax2 = rect2
    return [max(xmin1,xmin2), min(xmax1,xmax2), max(ymin1,ymin2), min(ymax1,ymax2)]
    
pos = (0,0,0,0)
    
for i in range(n):
    x, y = map(int,input().split())
    pos = plusd(pos,t)
    posnav = plusd((x+y,x+y,x-y,x-y),d)
    pos = intersect(pos, posnav)
    
points = []
for xPlusY in range(pos[0],pos[1]+1):
    for xMinusY in range(pos[2],pos[3]+1):
        if (xPlusY + xMinusY) % 2 == 0:
            x = (xPlusY + xMinusY) // 2
            y = xPlusY - x
            points.append((x,y))
            
print(len(points))
for point in points:
    print(*point)