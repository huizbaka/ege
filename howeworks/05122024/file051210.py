f = open('261.txt')

b = int(f.readline().split()[1])

A = []
B = []

c = []

for i in f:
    k = i.split()
    d = int(k[0])
    h = k[1]

    c.extend([(d, h)])

s = 0
c.sort()
e = 0

for p, q in c:

    if s + p <= b:

        if q == 'A':
            A.append(p)

        if q == 'B':
            e = e + 1

        s = s + p

    elif q == 'B' and s + p > b and len(B) <= len(A):
        B.append(p)

A.sort()
A = A[::-1]

B.sort()

for i in B:
    for j in range(len(A)):

        if s - A[j] + i <= b:
            s = s - A[j] + i
            e = e + 1
            A.pop(j)

            break

print(e, b - s)