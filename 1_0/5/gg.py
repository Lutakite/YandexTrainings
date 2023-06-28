n, k = map(int, input().split())
x = list(map(int, input().split()))

cards = dict()

for card in x:
    if card not in cards:
        cards[card] = 0
    cards[card] += 1
    #cards[card] = cards.get(card,0) + 1

result = 0
first_key = list(cards.keys())
first_key.sort()

#print(cards)
#print(first_key)

for i in range(0,len(first_key)):
    #print("i="+str(i))
    card = first_key[i]
    max = k*card
    if cards[card] > 2:
        result += 1
    #print(result)
    differentCards = 0
    for j in range(i+1, len(cards)):
        #print("j="+str(j))
        card2 = first_key[j]
        if card2 > max:
            break
        differentCards += 1
        if cards[card2] > 1:
            result += 3
        #print(result)
    #print("differentCards="+str(differentCards))
    #differentCards3 = 3*differentCards
    if cards[card] > 1:
        result += 3*differentCards
    result += 3*differentCards*(differentCards-1)
    #print(result)
print(result)