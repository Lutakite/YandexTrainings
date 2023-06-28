s = input().split()
n = int(s[0])
k = int(s[1])
m = int(s[2])

res = 0
m_in_k = k // m

while True:
    res_i = (n // k) * m_in_k
    if res_i == 0:
        break
    res += res_i
    n -= res_i * m

print(res)
