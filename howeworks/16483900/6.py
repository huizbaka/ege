target = 0
counter = 0

while target < 102:
    binary_repr = bin(counter)[2:]
    if counter % 2 == 0:
        binary_repr += "10"
    else:
        binary_repr += "01"

    target = int(binary_repr, 2)
    print(target)
    counter += 1
