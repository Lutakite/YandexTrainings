s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[2])

result = list()
for i in range(n+2):
    data = ["0" for j in range(m+2)]
    result.append(data)

ks = list()

for i in range(k):
    sk = input().split()
    p = int(sk[0])
    q = int(sk[1])
    #result[p][q] = "*"
    result[p+1][q] = str(int(result[p+1][q])+1)
    result[p-1][q] = str(int(result[p-1][q])+1)
    result[p+1][q+1] = str(int(result[p+1][q+1])+1)
    result[p-1][q+1] = str(int(result[p-1][q+1])+1)
    result[p+1][q-1] = str(int(result[p+1][q-1])+1)
    result[p-1][q-1] = str(int(result[p-1][q-1])+1)
    result[p][q+1] = str(int(result[p][q+1])+1)
    result[p][q-1] = str(int(result[p][q-1])+1)
    ks.append(sk)

for mina in ks:
    result[int(mina[0])][int(mina[1])] = "*"
        
    
for i in range(1,n+1):
    print(' '.join(result[i][1:m+1]))
    #str = ""
    #for j in range(1,m+1):
    #    print(result[i][j])
    #    str += result[i][j]
    #print(str)
        