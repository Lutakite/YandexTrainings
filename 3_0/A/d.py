xl, xr = map(int, input().split())
R = int(input())
n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]

def can_fit(d): 
    for x, y in coords: 
        if (x - d/2 <= xl + R or x + d/2 >= xr - R): 
            return False## Круг не помещается в проход 
        if (y**2 >= (R + d/2)**2 - (xl - x)**2) and (y**2 >= (R + d/2)**2 - (xr - x)**2):
            continue
        else: 
            return False
        return True

start, end = 0, 2 * (xr - xl)
while end - start > 1e-3:
    mid = (start + end) / 2 
    if can_fit(mid): 
        start = mid 
    else: 
        end = mid 
print("{:.3f}".format(start)) # Выводим максимальный диаметр круга с точностью до 3 знаков после запятой.