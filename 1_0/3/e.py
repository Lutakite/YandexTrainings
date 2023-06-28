s = input().split()
calc = set()
calc.add(s[0])
calc.add(s[1])
calc.add(s[2])
result = set()
s = input()
for i in s:
    if i not in calc:
        result.add(i)
print(len(result))
