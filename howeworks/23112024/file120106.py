# *31*65?
# 62961

a = 31 * 2031
b = ''
c = []
d = []


def delitl(x):
    k = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            k.append(i)
    return len(k)


for i in range(1000000000 // (a)):
    b = str(i * a)
    if ('31' in b) and (b[-3:-1] == '65'):
        c.append(int(b))

for i in c:
    print(delitl(i) + 1, i, i // 2031)


