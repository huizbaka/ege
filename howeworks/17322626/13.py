count = 0
for x in range(2**11):
    s = bin(x)[2:]
    if (8 + s.count('1'))%5 != 0:
        count += 1
print(count)