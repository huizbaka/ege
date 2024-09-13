trigger = 0
n = 1

while trigger < 97:
    bn = str(bin(n))[2:]
    a = sum(list(map(int, bn)))
    bn += str(a % 2)

    a = sum(list(map(int, bn)))
    bn += str(a % 2)

    trigger = int(bn, 2)
    n += 1

print(trigger)