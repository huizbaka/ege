f = open('69927.txt').read().split()
a = []
b = 0
c = 0
m = 0

for i in range(12000):
    k = int(f[i])
    a.append(k)
    if k % 32 == 0:
        b = b + 1

for i in range(1, 12000):
    if (a[i] + a[i - 1] < b) and ((a[i] < 0) or (a[i - 1] < 0)):
        c = c + 1
        if a[i] + a[i - 1] > m:
            m = a[i] + a[i - 1]

print(c, m)