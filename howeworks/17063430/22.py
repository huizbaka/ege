def win(x, y, step):
    if (step == 3 or step == 5) and x + y >= 59:
        return True
    if step == 5 and x + y < 59:
        return False
    if x + y >= 59 and step < 5:
        return False

    if step % 2 == 0:
        return (
            win(x + 1, y, step + 1) or
            win(x, y + 1, step + 1) or
            win(x * 2, y, step + 1) or
            win(x, y * 2, step + 1)
        )
    else:
        return (
            win(x + 1, y, step + 1) and
            win(x, y + 1, step + 1) and
            win(x * 2, y, step + 1) and
            win(x, y * 2, step + 1)
        )


def must_win(x, y, step):
    if step == 3 and x + y >= 59:
        return True
    if step == 3 and x + y < 59:
        return False
    if x + y >= 59 and step < 3:
        return False

    if step % 2 == 0:
        return (
            must_win(x + 1, y, step + 1) or
            must_win(x, y + 1, step + 1) or
            must_win(x * 2, y, step + 1) or
            must_win(x, y * 2, step + 1)
        )
    else:
        return (
            must_win(x + 1, y, step + 1) and
            must_win(x, y + 1, step + 1) and
            must_win(x * 2, y, step + 1) and
            must_win(x, y * 2, step + 1)
        )


for x in range(1, 54):
    if win(x, 5, 1):
        print(x)

print("====")

for x in range(1, 54):
    if must_win(x, 5, 1):
        print(x)