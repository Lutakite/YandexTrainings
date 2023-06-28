s1 = input()
s2 = input()

s1 = " "+s1
s2 = " "+s2
dp = list()
#dp.append([0]*(len(s2)+1))
for i in range(0, len(s1)):
    dp.append(list())
    #dp[i].append(0)
    #print(dp)
    for j in range(0, len(s2)):
        dp[i].append(0)
        if s1[i] == s2[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1]
        else:
            a = 1001
            b = 1001
            c = 1001
            if i > 0 and j > 0:
                a = dp[i-1][j-1]
            if i > 0:
                b = dp[i-1][j]
            if j > 0:
                c = dp[i][j-1]
            dp[i][j] = min(a, b, c)+1
    #print(dp)
#print(dp)
print(dp[len(s1)-1][len(s2)-1])      