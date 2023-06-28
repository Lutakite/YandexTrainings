n = int(input())
min = float(30)
max = float(4000)

fi_1 = float(input())

for i in range(n-1):
    s = input().split()
    fi = float(s[0])
    m = (fi_1+fi)/2
    #print(m)
    if (fi > fi_1):
        if s[1] == "further":
            if m < max:
                max = m
        else:
            if m > min:
                min = m
    else:
        if s[1] == "closer":
            if m < max:
                max = m
        else:
            if m > min:
                min = m
    #if (s[1] == "closer" and fi_1 <= fi) or (s[1] == "further" and fi_1 >= fi):
    #    print("change max")
    #    if m < max:
    #        max = m
    #else:
    #    print("change min")
    #    if m > min:
    #        min = m
    fi_1 = fi
            
print(str(min)+" "+str(max))
