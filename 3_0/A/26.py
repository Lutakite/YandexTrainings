n, m = map(int, input().split())

sq = [[-1, -2], [-2, -1], [-2,1], [1, -2]]
#print(rows)
dp = list()
for i in range(n):
    dp.append([0]*m)
#print(dp)
dp[0][0] = 1
#for i in range(n):
for t in range(m*n+1):
    for i in range(n):
        j = t - i
        if j >= m or j < 0:
            continue
        #print("t="+str(t)+"; i="+str(i)+ "; j="+str(j))
    #for j in range(m):
        if i==0 and j==0:
            continue
        for k in range(len(sq)):
            pi = i + sq[k][0]
            pj = j + sq[k][1]
            #print("pi="+str(pi))
            #print("pj="+str(pj))
            if pi >= 0 and pj >= 0 and pi < n and pj < m:
                #print("i="+str(i))
                #print("j="+str(j)) 
                #print("pi="+str(pi))
                #print("pj="+str(pj))
                dp[i][j] += dp[pi][pj]
                #print("dp[i][j]="+str(dp[i][j])
    #for line in dp:
    #    print(line)
#for i in range(len(dp)):
#    for j in range(
#for line in dp:
#    print(line)
print(dp[n-1][m-1])