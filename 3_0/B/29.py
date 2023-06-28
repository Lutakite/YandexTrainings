n = int(input())

prices = list()
for _ in range(n):
    prices.append(int(input()))
#print(prices)
#день, купон, деньги
sq = [[-1, -1, 1, 100], [-1, 1, 0, -1], [-1, 0, 1, -1]]
dp = list()
coupons = list()
for i in range(n+1):
    dp.append([-1]*(n+1))
    coupons.append([0]*(n+1))
#print(dp)
dp[0][0] = 0
coupons[0][0] = 0
for i in range(1, n+1):
    for j in range(n+1):
        #if i==0 and j==0:
        #    continue
        for k in range(len(sq)):
            pi = i + sq[k][0]
            pj = j + sq[k][1]
            #print("pi="+str(pi))
            #print("pj="+str(pj))
            if pi >= 0 and pj >= 0 and pi < n and pj < n and dp[pi][pj] > -1 and prices[i-1] > sq[k][3]:
                #print("i="+str(i))
                #print("j="+str(j))
                #print("pi="+str(pi))
                #print("pj="+str(pj))
                possible = dp[pi][pj] + sq[k][2]*prices[i-1]
                if dp[i][j] < 0 or possible < dp[i][j]:
                    dp[i][j] = possible
                    coupons[i][j] = sq[k][1]
                #print("dp[i][j]="+str(dp[i][j]))
#print(dp)
#print(coupons)
#for i in range(len(dp)):
#    for j in range(
res = dp[n][0]
k1 = 0
for i in range(1,n+1):
    if dp[n][i] >= 0 and dp[n][i] <= res:
        res = dp[n][i]
        k1 = i
print(res)

#print(coupons)
travel = list()
i = n
j = k1
k2 = 0
travelresult = list()
if i>1 or j > 0:
    while True:
        #print("i="+str(i)+"; j="+str(j))
        #print(coupons[i][j])
        travel.append(coupons[i][j])
        if coupons[i][j] == 1:
            travelresult.append(str(i))
            k2 += 1
        j += coupons[i][j]
        i -= 1
        
        if i==0:
            break

print(k1, end=" ")
print(k2)
#print(travelresult)
print(' '.join(reversed(travelresult)))
