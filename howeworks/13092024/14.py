for x in range(13):
    n1 = 2 * 13**4 + 6 * 13**3 + x * 13**2 + 9 * 13 + 8
    n2 = 4 * 13**4 + x * 13**3 + 2 * 13**2 + 9 * 13 + 6
    if (n1+n2) % 34 == 0:
        print((n1+n2) // 34)
        break