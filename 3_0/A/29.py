m, n = map(int, input().split())

dp = list()
dp.append([0]*(m+1))
dp.append([1]*(m+1))
dp[1][0] = 0
for i in range(2,n+1):
    dp.append([0]*(m+1))
    for j in range(1, m+1):
        for k in range(1,j+1):
            dp[i][j] += dp[i-1][k]*dp[1][j-k]
            dp[i][j] += dp[i-1][k]*dp[1][j-k+1]
 
#print(dp) 
print(dp[n][m])