from collections import deque

# процедура поиска в ширину
def bfs(start):
    queue = deque([(start, 0)])  # очередь с начальным элементом
    visited = set([start])  # множество посещенных залов
    time_to = [-1] * (n + 1)  # массив времен, за которое можно дойти до каждого зала
    time_to[start] = 0  # время до стартового зала равно 0
    
    while queue:
        room, time = queue.popleft()
        for neighbor in graph[room]:
            if neighbor not in visited:
                visited.add(neighbor)
                time_to[neighbor] = time + 1
                queue.append((neighbor, time + 1))
    
    for robot_room in robot_rooms:
        if robot_room not in visited:
            return -1  # роботы не смогут собраться вместе
    
    return max(time_to[robot_room] for robot_room in robot_rooms)
            

n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # граф залов
for _ in range(k):
    room1, room2 = map(int, input().split())
    graph[room1].append(room2)
    graph[room2].append(room1)

m = int(input())
robot_rooms = list(map(int, input().split()))

# обходим каждый зал с роботом
min_time = float('inf')
for room in robot_rooms:
    time = bfs(room)
    if time == -1:
        print(-1)
        break
    min_time = min(min_time, time)

else:  # если все роботы могут собраться вместе
    print(min_time)