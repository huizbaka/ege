a = {0: "А", 1: "Г", 2: "М", 3: "Н", 4: "С", 5: "Т", 6: "У"}
k = 0
maxi=[]
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                for n in range(0, len(a)):
                    for t in range(0, len(a)):
                        s = a[i] + a[j] + a[g] + a[m] + a[n] + a[t]
                        k += 1
                        if a[i] != 'У' and s.count('М') == 2 and s.count('Г') < 1:
                            maxi.append(k)
print(max(maxi))