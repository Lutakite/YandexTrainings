N, L = map(int,input().split())
lists = list()
for _ in range(N):
    li = list()
    x1, d1, a, c, m = map(int,input().split())
    li.append(x1)
    for i in range(1, L):
        #print(li[i-1]+d1)
        li.append(li[i-1]+d1)
        d1 = (a*d1+c)%m
    lists.append(li)
#print(lists)
def checkbigger(list, element):
    l = 0
    r = len(list)
    #print(list)
    #print("element="+str(element))
    while l < r and l < len(list):
        m = (l + r) // 2
        #print("m="+str(m))
        if list[m] >= element:
            r = m
        elif list[m] < element:
            l = m + 1
    #print(l+1)
    return (l+1)

def find(list1, list2):
    l = min(list1[0], list2[0])
    r = max(list1[L-1], list2[L-1])
    while l < r:
        m = (l + r) // 2
        #print("l="+str(l)+"; r="+str(r)+"; mmm="+str(m))
        result11 = checkbigger(list1, m)
        result21 = checkbigger(list2, m)
        #print("result11 = "+str(result11))
        #print("result21 = "+str(result21))
        result1 = result11 + result21 - 1
        if (result11 <= L and list1[result11-1] == m) or (result21 <= L and list2[result21-1] == m):
            #print("searching right")
            result12 = checkbigger(list1, m+1)
            result22 = checkbigger(list2, m+1)
            #print("result12 = "+str(result12))
            #print("result22 = "+str(result22))
            result2 = result12 + result22 - 2
            
            #print("result1 = "+str(result1))
            #print("result2 = "+str(result2))
            
            if result1 <= L and result2 >= L:
                l = m
                break
            else:
                if result1 > L:
                    r = m
                else:
                    l = m + 1
        else:
            if result1 > L:
                r = m
            else:
                l = m + 1
   
    #print(l)     
    return l

for i in range(N):
    for j in range(i+1, N):
        print(find(lists[i],lists[j]))