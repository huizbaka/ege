f = open('26_demo.txt')
data = f.readlines()
s = int(data[0].split()[0])
numbers = sorted([int(line.strip()) for line in data[1:]])

total = 0
count = 0
for num in numbers:
    if total + num > s:
        break
    total += num
    count += 1

remaining = s - total
for num in numbers:
    if num - numbers[count - 1] <= remaining:
        final = num

print(count, final)
