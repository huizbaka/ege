def can_reach_goal(x, steps, target_steps):
    if x <= 17:
        return steps in target_steps

    if steps >= max(target_steps):
        return False

    possible_moves = [can_reach_goal(x - 1, steps + 1, target_steps)]

    if x % 3 == 0:
        possible_moves.append(can_reach_goal(x // 3, steps + 1, target_steps))
    else:
        possible_moves.append(can_reach_goal(x - 2, steps + 1, target_steps))

    if x % 5 == 0:
        possible_moves.append(can_reach_goal(x // 5, steps + 1, target_steps))
    else:
        possible_moves.append(can_reach_goal(x - 3, steps + 1, target_steps))

    if steps % 2 != max(target_steps) % 2:
        return any(possible_moves)
    else:
        return all(possible_moves)


for x in range(17, 10000):
    if can_reach_goal(x, 0, [2]):
        print(x)
        break