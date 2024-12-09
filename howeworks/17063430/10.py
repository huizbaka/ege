lines = []
with open("10.txt") as file:
    for i in range(3100):
        line = file.readline()
        lines.append([int(x) for x in line.split()])
counter = 0

for i in lines:
    overall_sum = sum(i)
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]

    if max(i) < overall_sum - max(i):
        if (a + b == c + d) or (a + c == b + d) or (a + d == b + c):
           counter += 1
print(counter)