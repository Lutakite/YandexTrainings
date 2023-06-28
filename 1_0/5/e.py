n, k = map(int, input().split())
trees = list(map(int,input().split()))
#print(trees)
treesSeen = [0] * (k+1)

#print(treesSeen)
left = 0
right = 1

min = 250002
minl = 0
minr = 0
treesCount = 1
treesSeen[trees[0]] = 1
#print(treesSeen)
addRight = True
newLeft = True
if k != 1:
    while right < n and left <= right and left <= n-k:#left < n:
        #print("left = "+str(left)+"; rigth = "+str(right))
        if trees[left] == trees[right]:
            newLeft = True
            addRight = False
            left += 1
        while newLeft and left < n-k: #проверяем, правильный ли left\
            #print("checkleft")
            if treesSeen[trees[left]] != 1:
                treesSeen[trees[left]] -= 1
                left += 1
            else:
                newLeft = False
        #print("left = "+str(left)+"; rigth = "+str(right))
        #while left > right and right < n:
        #    right += 1
        #print("1:")
        #print(treesCount)
        #print(treesSeen)
        if addRight:
            treesSeen[trees[right]] += 1
            #print("2:")
            #print(treesSeen)
            if treesSeen[trees[right]] == 1:
                treesCount += 1
                #print("treesCount="+str(treesCount))
                if treesCount == k:
                    #print("bingo")
                    #print("bingo: left = "+str(left)+"; rigth = "+str(right))
                    if right - left < min:
                        min = right - left
                        minl = left
                        minr = right
                    treesCount -= 1
                    treesSeen[trees[left]] = 0
                    left += 1
                    newLeft = True
        right += 1
        addRight = True
print(str(minl+1) + " " + str(minr+1))