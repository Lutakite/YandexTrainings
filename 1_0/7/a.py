n, m = map(int, input().split())
#print(1)
#tables = [[0 for j in range(2)] for i in range(n+1)]#[[0]*2]*(n+1)
#print(2)
tables = dict()
for _ in range(m):
    b, c = map(int, input().split())
    if b not in tables:
        tables[b] = list()
        tables[b].append(0)
        tables[b].append(0)
    if c+1 not in tables:
        tables[c+1] = list()
        tables[c+1].append(0)
        tables[c+1].append(0)
    tables[b][0] += 1
    tables[c+1][1] -= 1
    #print(tables)  

#print(tables)

watchers = 0
result = 0
prev_table = 0
last_table = 0
nowatchers = True
for table in sorted(tables):
    watchers += tables[table][0] + tables[table][1]
    if watchers == 0 and nowatchers == False:
        prev_table = table
        nowatchers = True
    else:
        if nowatchers:
            result += table - prev_table
        nowatchers = False
    last_table = table

result += (n - last_table)
#for i in range(n):
#    watchers += tables[i][0] + tables[i][1]
#    if watchers < 0:
#        watchers = 0
#    if watchers == 0:
#        result += 1
print(result)