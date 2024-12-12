count = 0
for s in open('9_3.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(set(M)) == 5:
        copied = sum(M) - sum(set(M))
        if copied < (sum(M) - copied*2) / 4:
            count += 1
print(count)