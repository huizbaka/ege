for x in range(3022584,10**10):
    if x % 2024 == 0:
        y = x
        break
for x in range(y,10**10,2024):
    s=str(x)
    if s[0] == '3' and s[2:6] == '2258' and s[-1] == '4':
        print(x)