def sum_from_n(n):
    if n < 11:
        return n
    else:
        total = sum(range(11, n + 1))
        return total + 10

result = sum_from_n(2024) - sum_from_n(2021)
print(result)

