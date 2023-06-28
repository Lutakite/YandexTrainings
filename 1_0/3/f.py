a = input()
b = input()
agen = dict()
bgen = dict()
res = 0

for i in range(1,len(a)):
    gen = a[i-1] + a[i]
    agen[gen] = agen.get(gen, 0) + 1

for i in range(1,len(b)):
    gen = b[i-1] + b[i]
    bgen[gen] = bgen.get(gen, 0) + 1
    
for i in agen:
    if i in bgen:
        res += agen[i]

print(res)
