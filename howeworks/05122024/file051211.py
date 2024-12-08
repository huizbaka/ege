f = open('27-A.txt')

c = int(f.readline())
d = []
s = 0

def zxc(a):
    x = 0
    for i in range(1, 30):
        if a % (2 ** i) == 0:
            x = x + 1
        else:
            return x

def fye(b):
    y = 0
    for j in range(1, 14):
        if b % (5 ** j) == 0:
            y = y + 1
        else:
            return y

for i in range(c):
    k = int(f.readline())
    d.extend([(zxc(k), fye(k))])

for i, j in d:
    for p, q in d:
        if ((p + i == 7) and (q + j > 6)) or ((p + i > 6) and (q + j == 7)):
            s = s + 1

print(s // 2)