import heapq
n = int(input())
s = list(map(int, input().split()))

heapq.heapify(s)
result = 0

for _ in range(len(s)-1):
    a = heapq.heappop(s)
    b = heapq.heappop(s)
    sum = a + b
    result += sum*0.05
    heapq.heappush(s, sum)

print ("{0:.2f}".format(result))