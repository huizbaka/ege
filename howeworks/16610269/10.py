with open('09_2.xlsx') as file:
    count=0
    for line in file:
        n = list(map(int, line.split()))
        n.sort()
        if len(set(n)) == len(n) and \
        sum(x % 2 == 0 for x in n) > sum(x % 2 != 0 for x in n) and \
        sum(x for x in n if x % 2 == 0) < sum(x for x in n if x % 2 != 0):
            count += 1
print(count)