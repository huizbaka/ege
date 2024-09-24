number = 9**8 + 3**5 - 9
ternary_rep = ''
while number != 0:
    ternary_rep = str(number % 3) + ternary_rep
    number //= 3
print(ternary_rep.count("2"))
