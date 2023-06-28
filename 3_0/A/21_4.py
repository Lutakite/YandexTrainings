n = int(input())

#cubs = set()

res = [9]*(n+1)
#print(int(n**(1/3)))
for j in range(int(n**(1/3))+1, 0, -1):
    cub = j*j*j
    if cub > n:
        continue
    res[cub] = 1
    #cubs.add(iii)
    for i in range(n+1):
        if res[i] > 7:
            continue
        icub = i + cub
        if icub <= n:
            r = res[i]+1
            if r < res[icub]:
                res[icub] = r
            #res[icub] = min(res[icub], res[i]+1)
        else:
            break
#cubs = sorted(cubs)



#print("res = ", end="")
print(res[n])