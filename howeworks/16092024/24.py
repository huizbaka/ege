def longest_sequence_without_adjacent(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()

    max_length = 0
    current_length = 0

    for i in range(len(content)):
        if i > 0 and ((content[i] == 'a' and content[i - 1] == 'd') or (content[i] == 'd' and content[i - 1] == 'a')):
            max_length = max(max_length, current_length)
            current_length = 0
        else:
            current_length += 1

    max_length = max(max_length, current_length)
    return max_length

filename = '24.txt'
result = longest_sequence_without_adjacent(filename)
print(result)
