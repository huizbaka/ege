string = open('24.txt').read().strip()
string = string.replace('A', '*').replace('B', '*').replace('C', '*')
max_length = 1
current_length = 1

for i in range(1, len(string)):
    if string[i-1] + string[i] != '**':
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(max_length)
