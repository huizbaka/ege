def f(x):
    if x == 10:
        return 1
    if x < 10:
        return 0
    return f(x - 1) + f(x - 10)

print(f(31))