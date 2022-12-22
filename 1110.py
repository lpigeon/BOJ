# 더하기 사이클

import sys

n = int(sys.stdin.readline().rstrip())
i = 1

if n < 10:
        n = "0" + str(n)
new_n = str(n)

while True:
    sum_n = str((int(new_n[0])+int(new_n[1])))

    sum_n = int(sum_n)
    if sum_n < 10:
        sum_n = "0" + str(sum_n)
    sum_n = str(sum_n)

    new_n = str(new_n[1]) + str(sum_n[1])

    if int(n) == int(new_n):
        break
    
    new_n = int(new_n)
    if new_n < 10:
        new_n = "0" + str(new_n)
    new_n = str(new_n)

    i = i+1

print(i)