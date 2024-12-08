def fye(a, m):
    if a <= 19:
        return (m % 2 == 0)

    if m == 0:
        return 0

    h = [fye(a - 1, m - 1), fye((a // 3 if a % 3 == 0 else a - 2), m - 1),
         fye((a // 5 if a % 5 == 0 else a - 3), m - 1)]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print(19, ([s for s in range(20, 100) if fye(s, 2)]))
print(20, [s for s in range(20, 100) if not fye(s, 1) and fye(s, 3)])
print(21, [s for s in range(20, 100) if not fye(s, 2) and fye(s, 4)])