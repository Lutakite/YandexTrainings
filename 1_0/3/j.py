s = input().split()
t = int(s[0])
d = int(s[1])
n = int(s[2])

def gen_possible_positions(a, b, t):
    after_t = set()
    for i in range(-t,t+1):
        for j in range(-t,t+1):
            if abs(i)+abs(j) <= t:
                after_t.add((a+i,b+j))
    return after_t
    
    
    
currentpossiblepositions = set()
currentpossiblepositions.add((0,0))
    
for i in range(n):
    ipossiblepositions = set()
    s = input().split()
    near_d_positions = gen_possible_positions(int(s[0]),int(s[1]),d)
    for possibleposition in currentpossiblepositions:
        after_t_positions = gen_possible_positions(possibleposition[0],possibleposition[1],t)
        ipossiblepositions |= after_t_positions
    currentpossiblepositions = ipossiblepositions & near_d_positions

print(len(currentpossiblepositions))

#print(*sorted(bothset), sep=' ')
for i in currentpossiblepositions:
    print(' '.join(map(str,i)))
#   print(str(i[0])+str(" ")+str(i[1]))