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

r = 0
dups = 0
for l in range(len(first_key)):
    while r<len(first_key) and first_key[l]*k>=first_key[r]:
        if cards[first_key[r]] >= 2:
            dups += 1
        r += 1
    rangelen = r - l - 1
    if cards[first_key[l]] >= 2:
        result += 3*rangelen
        dups -= 1        
    if cards[first_key[l]] >= 3:
        result += 1
    result += 3*rangelen*(rangelen-1)
    result += 3*dups
            
print(result)