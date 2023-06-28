n = int(input())
tshirts = input().split()

m = int(input())
shorts = input().split()

bestchoice = abs(int(tshirts[0])-int(shorts[0]))
bestTshirt = tshirts[0]
bestShorts = shorts[0]
tshirtPos = 0
shortsPos = 0

while shortsPos < m and tshirtPos < n:
    choice = abs(int(tshirts[tshirtPos]) - int(shorts[shortsPos]))
    if choice < bestchoice:
        bestchoice, bestTshirt, bestShorts = choice, tshirts[tshirtPos], shorts[shortsPos]
    if int(tshirts[tshirtPos]) < int(shorts[shortsPos]):
        tshirtPos += 1
    else:
        shortsPos += 1

print(bestTshirt + " " + bestShorts)            