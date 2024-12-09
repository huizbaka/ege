from itertools import *

counter = 0
flag = 0
for i in product('012345678', repeat=11):
    s = ''.join(i)
    for i in s:
        if s.count(i) <= 4:
            flag += 1
    if "0" not in s and flag == len(s):
        for j in range(len(s) - 1):
            if s[j] % 2 != s[j+1] % 2:
                counter += 1
print(counter)