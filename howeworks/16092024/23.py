def program_counter(start, target):
    ways = [0] * (target + 1)
    ways[start] = 1

    for i in range(start, target + 1):
        if i + 1 <= target:
            ways[i + 1] += ways[i]
        if i + 10 <= target:
            ways[i + 10] += ways[i]

    return ways[target]

start_value = 10
target_value = 32
result = program_counter(start_value, target_value)
print(result)
