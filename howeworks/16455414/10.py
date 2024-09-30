characters = ["А", "К", "Р", "У"]
count = 0

for a in characters:
    for b in characters:
        for c in characters:
            for d in characters:
                for e in characters:
                    if count < 450:
                        count += 1
                        print(a, b, c, d, e, count)
