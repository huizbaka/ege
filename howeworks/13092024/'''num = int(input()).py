num = int(input())
m = sum(list(map(int, str(i))))
print(m)


for n in range (1,100):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    r = int(s, 2)
    if r > 43:
        print(r)
        break

