pool = 300

for a in range(0, pool):
    check = 0
    for x in range(0, pool):
        if (((x & 45 > 0) or (x & 89 > 0)) <= (x & a > 0)):
            check += 1
        if check == pool:
            print(a)