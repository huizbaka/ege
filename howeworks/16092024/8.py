from itertools import permutations

vowel_list = ['А', 'А', 'А', 'О']
consonant_list = ['П', 'Р', 'Б', 'Л']

def validate_code(seq):
    for i in range(len(seq) - 1):
        if (seq[i] in 'АО' and seq[i + 1] in 'АО') or (seq[i] not in 'АО' and seq[i + 1] not in 'АО'):
            return False
    return True

all_vowel_combos = set(permutations(vowel_list))
all_consonant_combos = set(permutations(consonant_list))

total_valid_codes = 0

for v_combo in all_vowel_combos:
    for c_combo in all_consonant_combos:
        combo1 = []
        combo2 = []
        for i in range(4):
            combo1.append(v_combo[i])
            combo1.append(c_combo[i])

            combo2.append(c_combo[i])
            combo2.append(v_combo[i])

        combo1 = ''.join(combo1)
        combo2 = ''.join(combo2)

        if validate_code(combo1):
            total_valid_codes += 1
        if validate_code(combo2):
            total_valid_codes += 1

print(total_valid_codes)
