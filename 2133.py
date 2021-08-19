n = int(input())
if n%2 != 0:
    print(0)
else:
    dp = [0 for _ in range(n+1)]
    dp[2] = 3
    for i in range(4, n+1, 2):
        for j in range(2, i-2, 2):
            dp[i] += dp[j]*2
        dp[i] += dp[i-2] * dp[2]
        dp[i] += 2
    print(dp[-1])
