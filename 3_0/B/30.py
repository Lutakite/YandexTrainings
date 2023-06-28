n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()

dp = list()
for i in range(n+1):
    dp.append([0]*(m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1] == s2[j-1]:
            #print("i="+str(i))
            #print("j="+str(j))
            dp[i][j] = dp[i-1][j-1]+1
        else:
            #print("here")
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

#print(dp)
res = dp[n][m]

reslist = list()
if res != 0: 
    #print(res)

    i = n
    j = m
    while i > 0 and j > 0 and dp[i][j] != 0:
        if dp[i-1][j] == res:
            i -= 1
        elif dp[i][j-1] == res:
            j -= 1
        else:
            reslist.append(s1[i-1])
            res -= 1
            i -= 1
            j -= 1

    print(' '.join(reversed(reslist)))
        