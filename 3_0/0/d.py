n = int(input())
k = int(input())
row = int(input())
column = int(input())

id1 = (row-1)*2+column
var = (id1)%k
if var == 0:
    var = k
id0 = id1 - k
id2 = id1 + k

prev_var_row = -1
prev_var_column = 0
next_var_row = -1
next_var_column = 0

if id0 > 0:
    if id0 % 2 == 0:
        prev_var_row = id0 // 2
        prev_var_column = 2
    else:
        prev_var_row = id0 // 2 + 1
        prev_var_column = 1
if id2 <= n:
    if id2 % 2 == 0:
        next_var_row = id2 // 2
        next_var_column = 2
    else:
        next_var_row = id2 // 2 + 1
        next_var_column = 1

if prev_var_row == -1 and next_var_row == -1:
    print(-1)
elif prev_var_row == -1:
    print(str(next_var_row)+" "+str(next_var_column))
elif next_var_row == -1:
    print(str(prev_var_row)+" "+str(prev_var_column))
elif abs(row - prev_var_row) < abs(row - next_var_row):
    print(str(prev_var_row)+" "+str(prev_var_column))
else:
    print(str(next_var_row)+" "+str(next_var_column))
    
#prev_var_row = 
#prev_var_column = 
#next_var_row = 
#next_var_column = 
#print(var)