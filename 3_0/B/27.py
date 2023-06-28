n, m = map(int, input().split())
rows = list()
for _ in range(n):
    rows.append(list(map(int, input().split())))

sq = [[-1, 0, "D"], [0, -1, "R"]]
dp = list()
res = list()
for i in range(n):
    dp.append([-1]*m)
    res.append([""]*m)
dp[0][0] = rows[0][0]

#travel = [""]*(n+m)
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        for k in range(len(sq)):
            pi = i + sq[k][0]
            pj = j + sq[k][1]
            if pi >= 0 and pj >= 0:
                possible = dp[pi][pj]+rows[i][j]
                if possible > dp[i][j]:
                    #print("i="+str(i)+"; j="+str(j)+"; sq="+str(sq[k][0])+str(sq[k][1])+str(sq[k][2]))
                    dp[i][j] = possible
                    res[i][j] = sq[k][2]
print(dp[n-1][m-1])
#print(res)
travel = list()
i = n-1
j = m-1
if i>0 or j > 0:
    while True:
        travel.append(res[i][j])
        if res[i][j] == "D":
            i -= 1
        else:
            j -= 1
        if i==0 and j==0:
            break

    print(' '.join(reversed(travel)))