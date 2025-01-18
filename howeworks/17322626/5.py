def f(n):
    for i in range(3):
        n = 2 * n + sum(map(int, str(n))) % 2
    return n
a, b = 123456789, 1987654321
n = a // 8 - 5
m = b // 8 - 5
while f(n) < a: n += 1
while f(m) <= b: m += 1
print(m - n)