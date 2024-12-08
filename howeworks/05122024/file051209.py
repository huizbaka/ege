f = open('26.txt')

a = int(f.readline())
c = 0

z = []

for i in range(604801):
    z.append(0)

for i in f:

    k = i.split()
    b = int(k[0])
    d = int(k[1])

    if (b < 1634515199) and ((d > 1634515199) or (d == 0)):
        c = c + 1

    if (b >= 1634515199) and (b <= 1634515199 + 604800):
        z[b - 1634515199] = z[b - 1634515199] + 1

    if (d >= 1634515199) and (d <= 1634515199 + 604800):
        z[d - 1634515199] = z[d - 1634515199] - 1

s = 0
mx = 0

for i in range(1, 604801):

    c = c + z[i] - z[i - 1]

    if c > mx:
        mx = c
        s = 0

    if c == mx:
        s = s + 1

print(mx, s)