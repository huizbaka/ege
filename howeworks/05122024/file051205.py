a = open('17.txt').read().split()

f = []
c = 0

mx = 0
mxx = 0

for i in range(len(a)):

    a[i] = int(a[i])

    if a[i] % 1000 == 123:
        mx = max(a[i], mx)

for i in range(2, len(a)):
    b = str(a[i - 2] % 3) + str(a[i - 1] % 3) + str(a[i] % 3)
    d = 0
    for j in [a[i - 2], a[i - 1], a[i]]:
        if j > 9999:
            d = d + 1

    if b.count('0') == 1 and d > 1 and (a[i - 2] + a[i - 1] + a[i] > mx):
        c = c + 1
        mxx = max(mxx, a[i - 2] + a[i - 1] + a[i])
# for i in f:
#    if i > mx:
#        c = c + 1

print(mxx, c)