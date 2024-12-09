def f(start, target):
    if start < target:
        return 0
    if start == target:
        return 1
    else:
        return f(start - 2, target) + f(start // 2, target) + f(start // 3, target)
print(f(38, 12) * f(12, 3))