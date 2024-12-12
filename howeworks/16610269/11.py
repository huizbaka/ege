f = open('9_1.txt')
count = 0
for line in f:
    numbers = list(map(int, line.split()))
    mx = max(numbers)
    s_nmx = sum(numbers) - mx
    if mx < s_nmx and len(set(numbers)) == 4:
        count += 1
print(count)