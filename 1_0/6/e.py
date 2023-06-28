a = int(input())
b = int(input())
c = int(input())

res = a*2 + b*3 + c*4

max = 100000000000000000
   
def countrec(a, w):
    return w // a

def find(a, b, c, res):
    l = 0
    r = max
    while l < r:
        m = (l + r) // 2
        print(m)
        check = (m*5 + res) / (a+b+c+m)
        print(check)
        if check > 3.5:
            r = m
        elif check < 3.5:
            l = m + 1
        else:
            l = m
            break
    return l

print(find(a,b,c,res))