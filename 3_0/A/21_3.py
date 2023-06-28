n = int(input())

cubs = set()

res = [9]*(n+1)
for i in range(1, int(n**(1/3))+1):
    iii = i*i*i
    res[iii] = 1
    cubs.add(iii)

cubs = sorted(cubs)

for i in range(n+1):
    for cub in cubs:
        icub = i + cub
        if icub <= n:
            res[icub] = min(res[icub], res[i]+1)
        else:
            break

#print("res = ", end="")
print(res[n])