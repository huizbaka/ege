def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 3, y) + f(x + 2, y)
print(f(2, 9) * f(9, 11) * f(11, 12))