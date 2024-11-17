r = []
for n in range(123456789, 456789012):
    if n % 2 == 1:
        a = "1" + str(bin(n))[2:] + "10"
    else: a = str(bin(n))[2:] + "11"
    print(n)
    r.append(int(a, 2))
print(max(r))