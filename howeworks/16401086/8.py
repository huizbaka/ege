chars = {0: "А", 1: "В", 2: "Л", 3: "О", 4: "Р"}
position = 0
for a in chars:
    for b in chars:
        for c in chars:
            for d in chars:
                position += 1
                if chars[a] == "Л":
                    print(position)
                    break
