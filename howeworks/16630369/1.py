a = {0: "К", 1: "Л", 2: "Р", 3: "Т"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                    k += 1
                    if k == 67:
                        print(a[i], a[j], a[g], a[m])