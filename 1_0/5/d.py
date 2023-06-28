n, r = map(int, input().split())
monuments = list(map(int, input().split()))

res = 0
left = 0
right = 0
while left < n:
    #if right == n-1:
    #    break
    distance = monuments[right+1] - monuments[left]
    #print("left="+str(left)+"; right="+str(right+1)+"; distance="+str(distance))
    if distance > r:
        res += n-right-1
        left += 1
    else:
        right += 1
        if right == n-1:
            break

print(res)