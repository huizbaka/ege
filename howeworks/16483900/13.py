def replace_substring(s, old_val, new_val):
    return s.replace(old_val, new_val, 1)


def process_string(s):
    while "00" not in s:
        s = replace_substring(s, "01", "220")
        s = replace_substring(s, "02", "1013")
        s = replace_substring(s, "03", "120")
    return s


def get_max_length():
    for length in range(2, 1000):
        s = "0" + "1" * (length - 2) + "0"
        processed = process_string(s)

        ones_count = processed.count("1")
        twos_count = processed.count("2")

        if ones_count == 13 and twos_count == 18:
            return length

    return None


max_len = get_max_length()
print(max_len)
