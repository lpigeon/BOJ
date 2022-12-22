import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
n = int(sys.stdin.readline().rstrip())
original = []
suboriginal = []
command = []
j = 0
for _ in range(n):
    original.append(int(sys.stdin.readline().rstrip()))

# 1부터 n까지 값을 suboriginal에 넣으며 original과 비교
# 만약, 값이 일치하면 pop을 값이 달라질때까지 반복
for i in range(n):
    command.append("+")
    suboriginal.append(i+1)
    if original[j] == suboriginal[-1]:
        while original[j] == suboriginal[-1]:
            command.append("-")
            suboriginal.pop()
            j += 1
            if len(suboriginal) == 0:
                break
            
# 위 반복문이 끝났을때 suboriginal에 값이 남아있으면 NO출력
# 아니면 command출력
if len(suboriginal) == 0:
    for i in range(len(command)):
        print(command[i])
else:
    print("NO")




            
et = time.time()
print("time : {:.4f}".format(et-st))