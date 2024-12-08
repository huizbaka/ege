def fye(x):
    a = 0

    if x + 1 > 8:
        return 1

    if x + 3 == 10:
        return 2

    a = a + fye(x + 1)
    a = a + fye(x + 3)

    if x * 2 <= 10:
        a = a + fye(x * 2)
    return a


print(fye(2) * 3)