f = open('9.xlsx')
count = 0
for s in f:
    a = list(map(int, s.split()))
    if len(set(a)) == len(a):
        sr1 = (min(a) + max(a))/2
        sr2 = (sum(a) - max(a) - min(a)) / 4
        if sr1 > sr2:
            count += 1
print(count)