for n in range(4):
    for k in range(10):
        for i in range(10**n):
            number = 10**(6 + n) + k * 10**(5 + n) + 954 * 10**(2 + n) + i * 10**2 + 21
            if number % 3147 == 0:
                print(number)
