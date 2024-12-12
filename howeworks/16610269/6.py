for n in range(2, 10000):
    s = bin(n)[2:]
    s = str(s)
    s = s[:-1]
    if n % 2 != 0:
        s += "10"
    else:
        s += "01"
    r = int(s, 2)  
    if r == 2018:
        print(n)