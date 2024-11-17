def f(n):
    if n < 15:
        return n
    else:
        return f(n % 15) * f(n // 15)
n = 0
check = 0
while n < 3 ** 40:
    if f(n) == 7560:
        check += 1
    n += 1
    print(n, check)