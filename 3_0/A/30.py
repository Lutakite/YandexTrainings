l, n = map(int, input().split())
c = list(map(int, input().split()))
c.insert(0,0)
c.append(l)

n += 2

dp = list()
for i in range(n):
    dp.append([0]*(n))

for i in range(2, n):
    dp[i-2][i] = c[i] - c[i-2]
#print(dp)
for t in range(3, n):
    for i in range(0, n-2):
        j = i + t
        if j >= n:
            break
        dp[i][j] = 100000006
        #print("i="+str(i))
        #print("j="+str(j))
        for k in range(i+1,j):
            #print("k="+str(k))
            #print(dp[i][k]+dp[k][j])
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        dp[i][j] += c[j]-c[i]
        #print(dp[i][j])
print(dp[0][n-1])
#print(dp)



