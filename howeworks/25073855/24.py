with open("1.txt", "r") as file:
    data = file.read().strip()

max_length = 0
cur = 0
start = 0
for end in range(len(data)):
    if end >= 3 and data[end - 3:end + 1] == "FSRQ":
        cur += 1
    while cur > 80:
        if start <= end - 3 and data[start:start + 4] == "FSRQ":
            cur -= 1
        start += 1
    if cur == 80:
        max_length = max(max_length, end - start + 1)

print(max_length)
