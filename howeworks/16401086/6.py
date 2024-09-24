count = 0
for num in range(1000, 10000):
    digits = str(num)
    if all(int(d) % 2 != 0 for d in digits):
        part1 = int(digits[0]) + int(digits[1])
        part2 = int(digits[2]) + int(digits[3])
        result = ''.join(map(str, sorted([part1, part2])))
        if result == '616':
            count += 1
print(count)
