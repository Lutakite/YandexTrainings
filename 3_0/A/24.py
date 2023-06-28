n = int(input())

worktime = list()
secondsprev = 0
prevtime = 0
for i in range(n):
    s = input().split()
    #print(s[1])
    p = int(s[1])
    time = s[0].split(":")
    h = int(time[0][0])*10+int(time[0][1])
    m = int(time[1][0])*10+int(time[1][1])
    s = int(time[2][0])*10+int(time[2][1])
    seconds = h*3600 + m*60 + s - 32400
    if i > 0:
        for _ in range(secondsprev, seconds):
            worktime.append(prevtime)
        #print(len(worktime))
    
    secondsprev = seconds
    #print(s[1])
    prevtime = p
    
    if i == n-1:
        seconds = 32400
        for _ in range(secondsprev, seconds):
            worktime.append(prevtime)
#print(len(worktime))
result = [0]*32401
for i in range(0, 14401):
    result[i+1] = max(result[i+1], result[i])
    if i+worktime[i] < 14401:
        result[i+worktime[i]] = max(result[i+worktime[i]], result[i]+1)
for i in range(18000, 32400):
    result[i+1] = max(result[i+1], result[i])
    if i+worktime[i] < 32401:
        result[i+worktime[i]] = max(result[i+worktime[i]], result[i]+1)

print(result[14400]+result[32400])