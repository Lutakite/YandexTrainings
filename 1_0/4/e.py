n = int(input())

blocks = dict()
for _ in range(n):
    s = input().split()
    width = int(s[0])
    height = int(s[1])
    if blocks.get(width,0) < height:
        blocks[width] = height

res = 0
for height in blocks.values():
    res += height
print(res)