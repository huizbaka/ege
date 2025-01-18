def to_base_3(n):
    base_3 = ""
    while n > 0:
        base_3 = str(n % 3) + base_3
        n //= 3
    return base_3 or "0"

def from_base_3(base_3_str):
    return int(base_3_str, 3)

def process_number(n):
    base_3 = to_base_3(n)
    if n % 3 == 0:
        # Если делится, на дописываем две последние цифры
        result = base_3 + base_3[-2:]
    else:
        # Если не делится на 3, считаем сумму цифр и переводим в троичную систему
        digit_sum = sum(int(digit) for digit in base_3)
        result = base_3 + to_base_3(digit_sum)
    return from_base_3(result)

for n in range(1, 1000):
    r = process_number(n)
    if r > 220 and r % 2 == 0:
        print(r)
        break
