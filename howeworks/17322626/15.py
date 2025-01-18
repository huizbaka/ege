count = 0
for a in range(1, 300):
    k = True
    for x in range(0, 300):
        for y in range(0, 300):
            if not(((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))):
                k = False
                break
    if k:
        count += 1
print(count)