a = {0: "А", 1: "Г", 2: "И", 3: "Л", 4: "М", 5: "О", 6: "Р", 7: "Т"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                k += 1
                if a[i] == 'И' and a[j] == 'Г':
                    print(k) 