n, m = map(int, input().split())
rows = list()
for _ in range(n):
    rows.append(list(map(int, input().split())))

sq = [[-1, 0], [0, -1]]
#print(rows)
dp = list()
for i in range(n):
    dp.append([50000]*m)
#print(dp)
dp[0][0] = rows[0][0]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        for k in range(len(sq)):
            pi = i + sq[k][0]
            pj = j + sq[k][1]
            #print("pi="+str(pi))
            #print("pj="+str(pj))
            if pi >= 0 and pj >= 0:
                #print("i="+str(i))
                #print("j="+str(j))
                #print("pi="+str(pi))
                #print("pj="+str(pj))
                dp[i][j] = min(dp[i][j], dp[pi][pj]+rows[i][j])
                #print("dp[i][j]="+str(dp[i][j]))
    #print(dp)
#for i in range(len(dp)):
#    for j in range(
#print(dp)
print(dp[n-1][m-1])