R_min = 1_111_111_110
R_max = 1_444_444_416

steps = [40, 40, 18]
cycle_length = sum(steps)

def calculate_R(N):
    binary = bin(N)[2:]
    mod3 = bin(N % 3)[2:].zfill(2)
    intermediate = int(binary + mod3, 2)
    mod5 = bin(intermediate % 5)[2:].zfill(3)
    R = int(binary + mod3 + mod5, 2)
    return R

N = 1
while True:
    R = calculate_R(N)
    if R >= R_min:
        if R <= R_max:
            first_N = N
            first_R = R
            break
    N += 1

count = 0
current_R = first_R
while current_R <= R_max:
    count += 1
    step = steps[(count - 1) % len(steps)]
    current_R += step

print("Количество подходящих чисел R:", count)