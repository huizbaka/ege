a = {0: "А", 1: "В", 2: "Е", 3: "И", 4: "К", 5: "Н", 6: "О", 7: "Р"}
k = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            s = a[i] + a[j] + a[g]
            if s.count('В') == 1:
                k += 1
                if s.count('А') == 0:
                    print(k)
                    break