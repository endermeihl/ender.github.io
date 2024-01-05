def prob_sum_less_than(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, min(j, 6)+1):
                dp[i][j] += dp[i-1][j-k]
    total = 6**n
    return sum(dp[n][:m]) / total

print(prob_sum_less_than(10,33))