def check_condition(a, b, level):
    if level == 3 and a + b >= 59:
        return True
    elif level == 3 and a + b < 59:
        return False
    elif a + b >= 59 and level < 3:
        return False
    else:
        if level % 2 == 0:
            return (check_condition(a + 1, b, level + 1) or
                    check_condition(a, b + 1, level + 1) or
                    check_condition(a * 2, b, level + 1) or
                    check_condition(a, b * 2, level + 1) )
        else:
            return (check_condition(a + 1, b, level + 1) or
                    check_condition(a, b + 1, level + 1) or
                    check_condition(a * 2, b, level + 1) or
                    check_condition(a, b * 2, level + 1) )

for start in range(1, 54):
    if check_condition(start, 5, 1):
        print(start)
        break