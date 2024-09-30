def count_paths(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return count_paths(x + 1, y) + count_paths(x * 3, y)

print(count_paths(3, 36))
