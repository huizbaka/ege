import openpyxl

workbook = openpyxl.load_workbook('18.xlsx')
active_sheet = workbook.active

data_table = []
for row in active_sheet.iter_rows(values_only=True):
    data_table.append(list(row))

size = len(data_table)
max_table = [[-float('inf')] * size for _ in range(size)]
min_table = [[float('inf')] * size for _ in range(size)]

max_table[0][0] = data_table[0][0]
min_table[0][0] = data_table[0][0]

for i in range(1, size):
    max_table[0][i] = max_table[0][i - 1] - data_table[0][i]
    min_table[0][i] = min_table[0][i - 1] - data_table[0][i]

    max_table[i][0] = max_table[i - 1][0] - 2 * data_table[i][0]
    min_table[i][0] = min_table[i - 1][0] - 2 * data_table[i][0]

for i in range(1, size):
    for j in range(1, size):
        hor_max = max_table[i][j - 1] - data_table[i][j]
        hor_min = min_table[i][j - 1] - data_table[i][j]

        ver_max = max_table[i - 1][j] - 2 * data_table[i][j]
        ver_min = min_table[i - 1][j] - 2 * data_table[i][j]

        max_table[i][j] = max(hor_max, ver_max)
        min_table[i][j] = min(hor_min, ver_min)

print(max_table[-1][-1], min_table[-1][-1])
