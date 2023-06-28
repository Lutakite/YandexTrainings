n, m = map(int, input().split())
cars = list(map(int, input().split()))

def countprefixsums(mass, length):
    result = [0] * (length + 1)
    for i in range(length):
        result[i+1] = result[i] + mass[i]
    return result
    
carssums = countprefixsums(cars, n)
#print(carssums)

res = 0
left = 0
right = 0
while right < n:
    sum = carssums[right+1] - carssums[left]
    #print("left="+str(left)+"; right="+str(right)+"; sum="+str(sum))
    if sum == m:
        res += 1
    if sum < m:
        right += 1
    else:
        left += 1

print(res)
