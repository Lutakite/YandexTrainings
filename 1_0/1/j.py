a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a != 0:
    if (d - c*b/a) != 0: # одно решение x,y
        y = (f - c*e/a) / (d - c*b/a)
        x = (e - b*y)/a
        print("2 "+str(x)+" "+str(y))
    else:
        if f - c*e/a == 0: # y любое
            if b == 0: # x один
                print("3 "+str(e/a))
            else: # y = kx + b
                print("1 "+str(-a/b)+" "+str(e/b))
        else: # решений нет
            print("0")
else: #a=0
    if b != 0:
        y = e/b
        if c != 0: # одно решение x,y
            x = (f - d*y)/c
            print("2 "+str(x)+" "+str(y))
        else: #c=0
            if d*y == f: # x любое
                print("4 "+str(y))
            else: # решений нет
                print("0")
    else: #a=0 && b=0
        if e != 0: # решений нет
            print("0")
        else: #cx+dy=f; dy = - cx + f
            if c != 0:
                if d != 0: #y = -c/d*x+f/d
                    print("1 "+str(-c/d)+" "+str(f/d))
                else: #cx=f
                    print("3 "+str(f/c))
            else: #dy = f
                if d != 0: #y = f/d, x любое
                    print("4 "+str(f/d))
                else: 
                    if f != 0: # решений нет
                        print("0")
                    else: # бесконечно решений
                        print(5)    
            