alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for first_char in alphabet[:9]:
    for second_char in alphabet[:9]:
        value_A = int(f'{first_char}341{second_char}', 11)
        value_B = int(f'56{first_char}1{second_char}', 19)
        print((value_A + value_B) / 305)
