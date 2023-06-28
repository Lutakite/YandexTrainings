n, m, k = map(int, input().split())

matrix = list()
matrix.append([0]*(m))
matrix.append(list(map(int, input().split())))
for i in range(2, n+1):
    ms = list(map(int, input().split()))
    matrix.append(list())
    for j in range(0, m):
        if i==1:
            matrix[i].append(ms[j])
        else:
            matrix[i].append(ms[j] + matrix[i-1][j])
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for i in range(y1-1, y2):
        #print("i="+str(i))
        #print(matrix[x2][i])
        #print(matrix[x1-1][i])
        #print()
        result += matrix[x2][i] - matrix[x1-1][i]
    print(result)