import openpyxl

workbook = openpyxl.load_workbook("107_9.xlsx")
sheet = workbook["09"]

count = 0

for i in range(1, sheet.max_row + 1):
    values = [sheet[f"A{i}"].value, sheet[f"B{i}"].value, sheet[f"C{i}"].value, sheet[f"D{i}"].value]

    max_val = max(values)
    min_val = min(values)
    values.remove(min_val)
    second_min = min(values)

    result = max_val - (min_val + second_min)

    if result > 0:
        count += 1


print(count)