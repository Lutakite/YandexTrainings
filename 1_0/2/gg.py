s = input().split()

max = 0
i_r = -1
j_r = -1
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        ij = int(s[i]) * int(s[j])
        if ij > max:
            max = ij
            i_r = s[i]
            j_r = s[j]

print(max)
print(i_r)
print(j_r)
    