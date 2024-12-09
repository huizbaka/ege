def evaluate_strategy(a, b, depth):
    if depth == 4 and a + b >= 59:
        return True
    elif depth == 4 and a + b < 59:
        return False
    elif a + b >= 59 and depth < 4:
        return False
    else:
        if depth % 2 == 1:
            return (evaluate_strategy(a + 1, b, depth + 1) or
                    evaluate_strategy(a, b + 1, depth + 1) or
                    evaluate_strategy(a * 2, b, depth + 1) or
                    evaluate_strategy(a, b * 2, depth + 1))
        else:
            return (evaluate_strategy(a + 1, b, depth + 1) and
                    evaluate_strategy(a, b + 1, depth + 1) and
                    evaluate_strategy(a * 2, b, depth + 1) and
                    evaluate_strategy(a, b * 2, depth + 1))

for start in range(1, 54):
    if evaluate_strategy(start, 5, 1):
        print(start)
        break