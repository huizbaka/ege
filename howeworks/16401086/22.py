def count_programs(start, end):
    dp = [0] * (end + 1)
    dp[end] = 1

    for i in range(end - 1, start - 1, -1):
        dp[i] = dp[i + 1] + (dp[i + 2] if i + 2 <= end else 0) + (dp[i + 5] if i + 5 <= end else 0)

    return dp[start]


start = 21
end = 30
print(count_programs(start, end))
