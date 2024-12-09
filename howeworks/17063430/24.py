def evaluate_strategy(x, depth, targets):
    if x <= 17:
        return depth in targets
    if depth >= max(targets):
        return False

    moves = [evaluate_strategy(x - 1, depth + 1, targets)]
    if x % 3 == 0:
        moves.append(evaluate_strategy(x // 3, depth + 1, targets))
    else:
        moves.append(evaluate_strategy(x - 2, depth + 1, targets))
    if x % 5 == 0:
        moves.append(evaluate_strategy(x // 5, depth + 1, targets))
    else:
        moves.append(evaluate_strategy(x - 3, depth + 1, targets))

    if depth % 2 != max(targets) % 2:
        return any(moves)
    else:
        return all(moves)


for x in range(17, 1000):
    if evaluate_strategy(x, 0, [1, 3]) and not evaluate_strategy(x, 0, [1]):
        print(x)