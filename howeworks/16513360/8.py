f = open('69914.txt')
ks = 0
for s in f:
    m=[int(x) for x in s.split()]
    p=[x for x in m if m.count(x)==3]
    n=[x for x in m if m.count(x)==1]
    if len(p) == 3 and len(n) == 3 and p[0] >= sum(n)/3:
        ks += 1
print(ks)