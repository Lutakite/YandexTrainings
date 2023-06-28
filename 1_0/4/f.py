from sys import stdin

d = dict()
for line in stdin:
    zakaz = line.split()
    buyer = zakaz[0]
    product = zakaz[1]
    count = int(zakaz[2])
    if buyer not in d:
        d[buyer] = dict()
    d[buyer][product] = d[buyer].get(product,0) + count

for buyer in sorted(d):
    print(buyer+':')
    for product in sorted(d[buyer]):
        print(product+" "+str(d[buyer][product]))