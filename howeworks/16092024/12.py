def optimized_max_n(target):
    for n in range(4, 10000):
        sequence = "5" + "2" * n

        sequence = sequence.replace("52", "11", 1)
        sequence = sequence.replace("2222", "5", 1)
        sequence = sequence.replace("1122", "25", 1)

        while "52" in sequence or "2222" in sequence or "1122" in sequence:
            if "52" in sequence:
                sequence = sequence.replace("52", "11", 1)
            if "2222" in sequence:
                sequence = sequence.replace("2222", "5", 1)
            if "1122" in sequence:
                sequence = sequence.replace("1122", "25", 1)

        if sum(map(int, list(sequence))) == target:
            return n
    return None

result = optimized_max_n(64)
print("Максимальное n:", result)
