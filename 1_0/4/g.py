from sys import stdin

d = dict()


for line in stdin:
    line = line.split()
    operation = line[0]
    if operation == 'DEPOSIT': #DEPOSIT name sum - зачислить сумму sum на счет клиента name Если у клиента нет счета, то счет создается
        name = line[1]
        sum = int(line[2])
        d[name] = d.get(name,0) + sum
    if operation == 'WITHDRAW': #WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет счета, то счет создается.
        name = line[1]
        sum = int(line[2])
        d[name] = d.get(name,0) - sum
    if operation == 'BALANCE': #BALANCE name - узнать остаток средств на счету клиента name.
        name = line[1]
        if name not in d:
            print("ERROR")
        else:
            print(d[name])
    if operation == 'TRANSFER': #TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается счет.
        name1 = line[1]
        name2 = line[2]
        sum = int(line[3])
        d[name1] = d.get(name1,0) - sum
        d[name2] = d.get(name2,0) + sum
       
    if operation == 'INCOME': #INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета. Проценты начисляются только клиентам с положительным остатком на счету, если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов сумма на счету остается целой, то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.
        p = int(line[1])
        for name in d:
            if d[name] > 0:
                d[name] += int(d[name]*p/100)
        