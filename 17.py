data = []

with open("17.txt") as f:
    for _ in range(5000):
        item = f.readline().strip()
        data.append(int(item))

print(data)

smallest_5 = min([num for num in data if abs(num) % 10 == 5])

pair_count = 0
max_square_sum = float('-inf')

for j in range(len(data) - 1):
    first, second = data[j], data[j + 1]

    if abs(first) % 10 == 5 and abs(second) % 10 != 5:
        smaller = first
    elif abs(second) % 10 == 5 and abs(first) % 10 != 5:
        smaller = second
    else:
        continue

    square_sum = first ** 2 + second ** 2
    if square_sum < smallest_5 ** 2:
        pair_count += 1
        max_square_sum = max(max_square_sum, square_sum)

print(pair_count, max_square_sum)