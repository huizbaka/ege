a = '012345678'
b = 0

for i in product(a, repeat=5):
    c = ''.join(i)
    if c[0] != '0' and ('21' not in c) and ('12' not in c) and ('23' not in c) and ('32' not in c) and (
            '25' not in c) and ('52' not in c) and ('27' not in c) and ('72' not in c) and c.count('3') == 2:
        b = b + 1

print(b)