#Делаем два индекса - левый и правый.

#Двигаем правый, подсчитывая количество каждого символа на текущий момент в словарь со счётчиком.

#Когда один из счётчиков становится больше k - останавливаемся, фиксируем длину как разницу правого и левого.

#Двигаем левый индекс, уменьшая счётчики для каждого символа. Когда счётчик с превышением уменьшается - останавливаемся, и начинаем снова двигать правый индекс. И т.д.

n, k = map(int, input().split())
s = input()

result = 0
l = 0
r = 0
resultL = 0
resultR = 0
resultLen = 0

countLetters = dict()
while r < n and l < n:
    #print("l="+str(l)+"; r="+str(r))
    countLetters[s[r]] = countLetters.get(s[r],0) + 1
    #print(countLetters)
    if countLetters[s[r]] > k:
        #print("here")
        if resultLen < r-l:
            resultLen = r-l
            resultL = l
            resultR = r
        while l<n and countLetters[s[r]] > k:
            countLetters[s[l]] -= 1
            l += 1
        #print(countLetters)
        #print(resultLen)
    r += 1
    if r==n:
        if resultLen < r-l:
            resultLen = r-l
            resultL = l
            resultR = r
        
    
print(str(resultLen)+" "+str(resultL+1))