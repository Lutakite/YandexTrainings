n = int(input())

points = list()
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
result = 0
for i in range(n):
    ros = list()
    usedpoints = set()
    for j in range(n):
        newx = points[j][0]-points[i][0]
        newy = points[j][1]-points[i][1]
        ro = newx**2 + newy**2
        if (newx, newy) in usedpoints:
            result -= 1
        usedpoints.add((-newx, -newy))
        ros.append(ro)
    ros.sort()
    r = 0
    for l in range(len(ros)):
        while r<len(ros) and ros[l] == ros[r]:
            r += 1
        result += r - l - 1
    #for ro in points2points:
    #    result += int(len(points2points[ro])*(len(points2points[ro]) - 1) / 2)

print(result)