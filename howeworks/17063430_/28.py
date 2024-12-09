with open('24.txt') as file:
    data = file.readline()

data = data.translate(str.maketrans('23456', '11111'))
data = data.replace('*', '-').replace('A', ' ').replace('C', ' ').replace('D', ' ')
data = data.replace('1B', '1 B').replace('--', '- -').replace('BB', 'B B')
data = data.replace('-B', '- B').replace('B-', 'B -')

sequences = sorted(data.split(), key=lambda x: -len(x))

for sequence in sequences:
    if sequence.startswith('B') and sequence.count('B') == 1:
        if sequence.endswith('-'):
            sequence = sequence[:-1]
        print(sequence, len(sequence))
        break