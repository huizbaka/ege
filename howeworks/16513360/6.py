cnt = 0
f = open('09.csv')
for s in f:
    a = list(map(int,s.split(';')))
    a.sort()
    if a[0]**2 + a[1]**2 > a[2]**2:
        cnt+=1
print(cnt)