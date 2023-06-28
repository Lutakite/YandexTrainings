def getNeighbours1(a, start):
    result = list()
    if start:
        if a < 9000:
            result.append(a+1000)
        if a%10 > 1:
            result.append(a-1)
    else:
        if a >= 2000:
            result.append(a-1000)
        if a%10 < 9:
            result.append(a+1)
    result.append((a%10)*1000+a//10)
    result.append((a%1000)*10+a//1000)
    return result
    
def bfs(start, finish, visited, mark):
    visited[start] = [0,0]
    queue = list()
    queue.append(start)
    done = False
    while not done and queue:
        s = queue.pop(0)
        for neighbor in getNeighbours1(s, mark):
            if neighbor not in visited:
                visited[neighbor] = [visited[s][0]+1, s]
                queue.append(neighbor)
            if neighbor == finish:
                done = True
                break
start = int(input())
finish = int(input())
visited1 = dict()
#visited2 = dict()
#result1 = dict()
#result2 = dict()
bfs(start, finish, visited1, True)
#print(visited1)
result = list()
last = finish
while last != start:
    result.append(str(last))
    last = visited1[last][1]
result.append(str(last))
print('\n'.join(reversed(result)))
#for i in range(1, visited1[finish][0]):
#    result.append(
#    last = visited1[
#bfs(finish, start, visited2, False, result2)
#print(start)
#for i in range(1, visited1[finish]+1):
    #print(result1[i])
    #print(result2[visited1[finish]-i])
#    print(list(result1[i] & result2[visited1[finish]-i])[0])
#print(finish)    
#print(visited1)
#print(visited2)
#print(getNeighbours1(1234,1))
        
    