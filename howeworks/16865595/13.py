for x in range(0, 8):
    for y in range(0, 8):
        num1 = (5 * 11) ** 0 + (x * 11) ** 1 + (4 * 11) ** 2 + (y * 11) ** 4
        num2 = (y * 8) ** 0 + (x * 8) ** 1 + (3 * 8) ** 2 + (5 * 8) ** 3 + (2 * 8) ** 4
        if (num1 + num2) % 117 == 0:
            print((num1 + num2) // 117, num1 + num2)