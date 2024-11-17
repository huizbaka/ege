from itertools import product


num_counter = 0

for i in product('x10',repeat = 8):
    s = "".join(i)
    if s[0] != '0' and s.count("0") == 2 and s.count("x") <= 4:
        num_counter += 9 ** s.count("1") * 6 ** s.count("x")
print(num_counter)