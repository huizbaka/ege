sizes = []

with open("27881.txt") as file:
    lines = file.readlines()
    space_left = int(lines[0].split()[0])
    sizes = list(map(int, lines[1:4627]))

sizes.sort()
index = 0

while space_left > 0 and index < len(sizes):
    current_size = sizes[index]
    print(current_size)
    if current_size > space_left:
        print(index, space_left, sizes[index])
        break
    space_left -= current_size
    index += 1

print(index, space_left)