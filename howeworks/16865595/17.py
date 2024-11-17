nums = [int(x) for x in open("17.txt")]
min_num = min(nums)
max_num = max(nums)


counter = 0
final_sum = 0
for i in range(len(nums) - 1):
    num1 = nums[i]
    num2 = nums[i+1]
    if (((num1 % 3 == min_num % 3) or (num2 % 3 == min_num % 3)) and ((num1 % 7 == max_num % 7) or (num2 % 7 == max_num % 7))):
        counter += 1
        final_sum = max(final_sum, num1 + num2)

print(counter, final_sum)
