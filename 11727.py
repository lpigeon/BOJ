# 2×n 타일링 2

# DP를 이용한 문제
# 크기가  i인 직사각형을 채우는 방법은
# 1. 크기가 i-1인 직사각형을 채우는 방법의 +1이다,(세로로 긴 사각형1개만 가능함)
# 2. 크기가 i-2인 직사각형을 채우는 방법의 *2이다.(가로로 긴 사각형 2개와, 정사각형 1개가 가능함)
# 그리고 마지막으로 dp[1],dp[2]만 수작업으로 채워준 뒤
# 점화식 dp[i]=dp[i-1]+ 2*dp[i-2];을 이용하여 값을 구합니다.
# 참고 : https://cijbest.tistory.com/21

import sys

n = int(sys.stdin.readline().rstrip())
dp = [0]*1001
dp[0] = 1
dp[1] = 3
dp[2] = 5
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[n-1]%10007)