m = int(input())
n = int(input())

sectors = {}

line = {}
for i in range(n):
    a, b = map(int, input().split())
    for sector in sectors:
        if (sectors[sector[0]] <= a and sectors[sector[1]] >= a) or (sectors[sector[0]] <= b and sectors[sector[1]] >= b):
            print("!!!!")
        