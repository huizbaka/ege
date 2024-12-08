def delitl(x):
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return i + (x // i)

    return 0


for i in range(452022, 452121):
    if delitl(i) % 7 == 3:
        print(i, delitl(i))