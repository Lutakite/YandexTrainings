n, a, b = map(int, input().split())
#res = 0
def count(x, a, b):
    #print("x="+str(x))
    if x == 1:
        return 0
    res = [0]*x
    for i in range(1,x):
        res[i] = min(max(a + count(x-i, a, b), b + count(i, a, b)), max(b + count(x-i, a, b), a + count(i, a, b)))
    ans = res[1]
    for i in range(2,x):
        if res[i] > ans:
            ans = res[i]
            
    return ans



print(count(n, a, b))
#if a==b:
#    res += a*ln(n)
#elif a==0:
#    res = b
#elif b==0:
#    res = a
#else: