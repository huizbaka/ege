a = {0: "А", 1: "Б", 2: "З", 3: "И"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                k += 1
                if i == 3 and j == 2 and g == 1 and m == 0:
                    print(k)