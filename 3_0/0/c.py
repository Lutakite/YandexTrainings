n = int(input())

def checksmaller(list, element):
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
    return (l)

diegoCards = list(set((map(int, input().split()))))
#print(diegoCards)
diegoCards.sort()

m = int(input())
cards = list(map(int, input().split()))
for card in cards:
    print(checksmaller(diegoCards, card))