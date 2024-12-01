f = open('1_24.txt').read()

a = 1
b = 1

for i in range(1, len(f)):

    if ((s[i] in '124' and s[i - 1] in 'QWR') or ((s[i] in 'QWR') and (s[i - 1] in '124'))):
        a = a + 1

    elif a > b:
        b = a
        a = 1
    else:
        a = 1

print(b)