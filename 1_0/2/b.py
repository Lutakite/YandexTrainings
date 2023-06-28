prev = int(input())
s = int(input())
result = ""
if s > prev:
    result = "ASCENDING"
elif s < prev:
    result = "DESCENDING"
elif s == prev:
    result = "CONSTANT"

while True:
    s = int(input())
    if s == -2000000000:
        break
    if s > prev:
        if result == "CONSTANT":
            result = "WEAKLY ASCENDING"
        elif result == "WEAKLY DESCENDING" or result == "DESCENDING":
            result = "RANDOM"
    elif s < prev:
        if result == "CONSTANT":
            result = "WEAKLY DESCENDING"
        elif result == "WEAKLY ASCENDING" or result == "ASCENDING":
            result = "RANDOM"
    elif s == prev:
        if result == "DESCENDING":
            result = "WEAKLY DESCENDING"
        elif result == "ASCENDING":
            result = "WEAKLY ASCENDING"
    prev = s
    if result == "RANDOM":
        break
        
print(result)
