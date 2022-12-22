# 피보나치 수 2

# 다이나믹 프로그래밍을 사용하여야 시간초과 안당함
import sys

n = int(sys.stdin.readline().rstrip())
dp = [i for i in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])