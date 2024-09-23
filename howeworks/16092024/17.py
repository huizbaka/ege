with open('17.txt') as file:
    data = list(map(int, file.readlines()))

pair_count = 0
largest_sum = 0

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        total_sum = data[i] + data[j]
        if total_sum % 120 == 0:
            pair_count += 1
            if total_sum > largest_sum:
                largest_sum = total_sum

print(pair_count)
print(largest_sum)
