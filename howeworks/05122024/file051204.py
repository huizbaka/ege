from itertools import *

a = '012'
b = 0

for i in product(a, repeat=5):
    c = ''.join(i)
    if c[0] != '0' and ('22' not in c) and ('11' not in c)and ('02' not in c) and ('20' not in c) and (c.count('0') < 2) and (c.count('1') < 4) and (c.count('2') < 4):
        if (c.count('2') == 1 and c.count('1') == 3) or (c.count('2') == 3 and c.count('1') == 1):
            b = b + 18
        elif c.count('2') == 2 and c.count('1') == 2:
            b = b + 36
        elif (c.count('2') == 2 and c.count('1') == 3) or (c.count('2') == 3 and c.count('1') == 2):
            b = b + 36

print(b)