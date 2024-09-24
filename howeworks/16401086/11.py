def prime_check(val):
    for div in range(2, val // 2 + 1):
        if val % div == 0:
            return False
    return True

for number in range(69, 100):
    calculated = number + number * 2 - 1
    if prime_check(calculated):
        print(number)
        break
