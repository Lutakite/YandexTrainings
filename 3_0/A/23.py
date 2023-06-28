n = int(input())

res = 0
k = n // 2
if n % 2 == 0:
    res = k*(k+1)*(4*k+1)//2
else:
    res = (k+1)*(4*k*k+7*k+2)//2
    
print(res)
