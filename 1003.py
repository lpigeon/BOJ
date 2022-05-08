# 피보나치 함수

import sys
t = int(sys.stdin.readline().rstrip())
                             
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        dp = [[1 for i in range(n + 1)] for j in range(2)]
        dp[0][1] = 0
        dp[1][0] = 0
        for i in range(3, n+1):
            dp[0][i] = dp[0][i-1] + dp[0][i-2]
        for i in range(2, n+1):
            dp[1][i] = dp[1][i-1] + dp[1][i-2]
        print(dp[0][n], dp[1][n])