sequence = "8" * 99 + "1"

str_a = "133"
str_b = "881"

while str_a in sequence or str_b in sequence:
    if str_a in sequence:
        sequence = sequence.replace(str_a, "81", 1)
    else:
        sequence = sequence.replace(str_b, "13", 1)

print(sequence)

