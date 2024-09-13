def find_longest_valid_sequence(text):
    allowed_characters = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWX")
    longest_length = 0
    i = 0
    text_length = len(text)

    while i < text_length:
        j = i
        while j < text_length and text[j] in allowed_characters:
            j += 1
        if i < j and (text[i] != '0' or i == j - 1):
            longest_length = max(longest_length, j - i)
        i = j + 1

    return longest_length

with open("24_59848.txt", "r") as file:
    content = file.read()

print(find_longest_valid_sequence(content))