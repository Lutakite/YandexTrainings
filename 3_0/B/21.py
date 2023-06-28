n = int(input())

s0 = [0]*n
s1 = [0]*n
s11 = [0]*n
sum = [0]*n

s0[0] = 1
s1[0] = 1
sum[0] = 2
for i in range(1,n):
    s0[i] = sum[i-1]
    s1[i] = s0[i-1]
    s11[i] = s1[i-1]
    sum[i] = s0[i] + s1[i] + s11[i]
    
print(sum[n-1])