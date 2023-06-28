#N, S, W, E, U и D 
def fromNSW(s):
    if s == 'N':
        return 0
    if s == 'S':
        return 1
    if s == 'W':
        return 2
    if s == 'E':
        return 3
    if s == 'U':
        return 4
    if s == 'D':
        return 5
        
def toNSW(s):
    if s == 0:
        return 'N'
    if s == 1:
        return 'S'
    if s == 2:
        return 'W'
    if s == 3:
        return 'E'
    if s == 4:
        return 'U'
    if s == 5:
        return 'D'

dict = list()
dict.append([""]*6)
dp = list()
dp.append([1]*6)
dict[0][0] = input()
dict[0][1] = input()
dict[0][2] = input()
dict[0][3] = input()
dict[0][4] = input()
dict[0][5] = input()
#print(dp)
a = input().split()
c = a[0]
n = int(a[1])

dp.append([0]*6)
for j in range(6):
    #result = toNSW(j) + dp[1][j]
    #dp[2][j] = result
    result = toNSW(j) + dict[0][j]
    dp[1][j] = len(result)

for i in range(2, n):
    dp.append([0]*6)
    #print(dp)
    for j in range(6):
        result = 1
        for k in range(len(dict[0][j])):
            result += dp[i-1][fromNSW(dict[0][j][k])]
        dp[i][j] = result
       
result = 1
j = fromNSW(c)
for k in range(len(dict[0][j])):
    result += dp[n-1][fromNSW(dict[0][j][k])]
#dp[i][j] = result
#print(dp)
#print(dp[n][fromNSW(c)])
print(dp[n-1][j])
