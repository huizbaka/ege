def from_base(number, base):
    return int(number, base)

num1_base = "11353012"
num2_base = "135021"
dec1_base = from_base(num1_base, 25)
dec2_base = from_base(num2_base, 25)
max_x = -1
res24 = -1

for x in range(25):
    dec2 = dec2_base + x * (25**2)
    dec1 = dec1_base + x * (25**2)
    expression_value = dec1 + dec2
    if expression_value % 24 == 0:
        max_x = x
        res24 = expression_value // 24

print(max_x)
print(res24)
