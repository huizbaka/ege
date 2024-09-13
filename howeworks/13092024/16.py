def f(x):
    if x > 2 and x % 2 == 1:
        return int((7*x + f(x - 1) - f(x-2)) / 5)
    if x > 2 and x % 2 == 0:
        return int((3*x + f(x-3))/3)
    if x == 1:
        return 1
    if x == 2:
        return 2

print(f(35))