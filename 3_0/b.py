n = int(input())

rackets = dict()
for _ in range(n):
    day, hour, minute, id, status = input().split()
    time = int(minute) + (int(day)-1)*24*60 + int(hour)*60
    #print(day+"."+hour+"."+minute)
    #print(time)
    #print((int(day)-1)*24*60)
    #print(int(hour)*24)
    racket = int(id)
    if racket not in rackets:
        rackets[racket] = dict()
    rackets[racket][time] = status

resultr = ""
for racket in sorted(rackets):
    result = 0
    count = 0
    #prev = "C"
    for time in sorted(rackets[racket]):
        if rackets[racket][time] == "S" or (rackets[racket][time] == "C"):
            result += time - count
            count = 0
        #elif rackets[racket][time] == "B":
        #    count = time
        elif rackets[racket][time] == "A":
            count = time
        #print("start="+str(count))
        #print(time)
        #print(rackets[racket][time])
        #print("result=")
        #print(result)
    resultr += str(result)+ " "
print(resultr[:len(resultr)-1])