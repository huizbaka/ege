start = (1021574 // 2024 + 1) * 2024

while start < 10**10:
    s = str(start)
    if s[0] == '1' and s[2:6] == '2157' and s[-1] == '4':
        print(f"{s} {start // 2024}")
    start += 2024