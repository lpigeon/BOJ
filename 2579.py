# 계단 오르기

# DP를 이용
# 계단 3개이상을 연속해서 밟을 수 없으므로
# 두가지 경우로 나눔
# 제일 마지막 계단은 무조건 밟아야 하므로 그 앞에 계단을 밟는경우
# 또는 그 앞앞 계단을 밟은 경우

import sys

n = int(sys.stdin.readline().rstrip())
dp = [0]*n
point = []
for i in range(n):
    point.append(int(sys.stdin.readline().rstrip()))

dp[0] = point[0]
dp[1] = point[0] + point[1]
dp[2] = max(point[0] + point[2], point[1] + point[2])
for i in range(3,n):
    dp[i] = max(dp[i-2] + point[i], dp[i-3] + point[i-1] + point[i])
print(dp[n-1])