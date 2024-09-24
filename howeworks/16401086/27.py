with open("27-B.txt") as f:
    data = f.readlines()
    n = int(data[0])

total_sum, sum2, sum3, min_diff = 0, 0, 0, 20001

for i in range(1, n + 1):
    x, y, z = map(int, data[i].split())
    minimum = min(x, y, z)
    total_sum += minimum
    if minimum == x:
        sum2 += min(y, z)
        sum3 += max(y, z)
        min_diff = min(min_diff, abs(x - y) if abs(x - y) % 2 != 0 else 20001)
    elif minimum == y:
        sum2 += min(x, z)
        sum3 += max(x, z)
        min_diff = min(min_diff, abs(y - z) if abs(y - z) % 2 != 0 else 20001)
    else:
        sum2 += min(x, y)
        sum3 += max(x, y)
        min_diff = min(min_diff, abs(z - x) if abs(z - x) % 2 != 0 else 20001)

if (sum2 + sum3) % 2 != 0:
    print(total_sum)
else:
    print(total_sum + min_diff)
