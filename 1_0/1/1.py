s = input().split()
mode = input()
s[0] = int(s[0])
s[1] = int(s[1])
res = s[0]
if mode == 'auto' or (mode == 'freeze' and s[1] < s[0]) or (mode == 'heat' and s[1] > s[0]):
	res = s[1]
print(res)
