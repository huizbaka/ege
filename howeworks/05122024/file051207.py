f = open('24.txt').read().replace('A', 'A ').replace('B', 'B ').split(' ')

mx = 0

for i in range(len(f) - 2):

    c = f[i] + f[i + 1] + f[i + 2][:-1]

    if c.count('A') == 1:
        mx = max(mx, len(c))

print(mx)