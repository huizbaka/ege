numb = 0
limit = 0

while limit < 100:
    binary = bin(numb)[2:]
    binary += str(sum(int(bit) for bit in binary) % 2)
    binary += str(sum(int(bit) for bit in binary) % 2)

    limit = int(binary, 2)
    numb += 1
    print(limit)
