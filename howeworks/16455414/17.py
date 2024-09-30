def compute_factorial(n):
    if n == 1 or n == 2:
        return 1
    return compute_factorial(n - 2) * n

print(compute_factorial(7))
