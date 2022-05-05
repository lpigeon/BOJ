# 단어 정렬
import sys

n = int(sys.stdin.readline().rstrip())
result = []
new_result = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    result.append(s)
result = list(set(result))

for i in result:
    new_result.append([i, len(i)])
new_result = sorted(new_result, key=lambda x: (x[1], x[0]))

for i in range(len(new_result)):
    print(new_result[i][0])