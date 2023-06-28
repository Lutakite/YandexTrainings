n, k = map(int, input().split())
from collections import deque
s = list(map(int, input().split()))

deque = deque()

for i in range(len(s)):
    if len(deque) > 0 and deque[0] <= i - k:
        deque.popleft()

    while len(deque) > 0 and s[deque[-1]] >= s[i]:
        deque.pop()

    deque.append(i)

    if i >= k - 1:
        print(s[deque[0]])