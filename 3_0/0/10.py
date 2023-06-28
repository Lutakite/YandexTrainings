s = input()
dict = {}
n = len(s)
for i in range(1, n+1):
    dict[s[i-1]] = dict.get(s[i-1],0) + (n - i + 1)*i

for d in sorted(dict):
    print(d+": "+str(dict[d]))
    
    