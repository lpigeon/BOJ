# 코딩은 체육과목 입니다.

import sys
n = int(sys.stdin.readline().rstrip())

a = n // 4

result = ""

for _ in range(a):
    result += "long "
    
result += "int"

print(result)