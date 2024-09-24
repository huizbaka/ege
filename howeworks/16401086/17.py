count_pairs = 0
maximum_sum = 0
with open('17.txt') as f:
    nums = list(map(int, f))

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 80 == 0 and (nums[i] % 50 == 0 or nums[j] % 50 == 0):
            count_pairs += 1
            maximum_sum = max(maximum_sum, nums[i] + nums[j])

print(count_pairs, maximum_sum)
