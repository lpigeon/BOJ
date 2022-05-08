# 집합

# 일반적인 set함수를 쓰면 시간초과 걸림
# 빠른 연산을 위해 비트마스킹 기법을 사용
import sys

# 총 1부터 20을 저장해야 하므로 길이가 20인 비트를 생성
s = 0b00000000000000000000
n = int(sys.stdin.readline().rstrip())


# 비트마스킹 기법
# 원소 추가 s |= (1 << num) num번째를 1로 세팅
# 원소 삭제 s &= ~(1 << num) num번째를 0으로 세팅
# 원소 토글 s ^= (1 << num) num번째를 1이면 0, 0이면 1로 세팅
# 원소 체크 print(1 if s & (1 << int(op[1])) != 0 else 0))
# 원소 비우기 & 채우기 s = 0 , s =(1 << 22) - 1
for _ in range(n):
    command = list(sys.stdin.readline().rstrip().split())
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == "add":
        s |= (1 << command[1])
    elif command[0] == "remove":
        s &= ~(1 << command[1])
    elif command[0] == "check":
        print(1 if s & (1 << command[1]) != 0 else 0)
    elif command[0] == "toggle":
        s ^= (1 << command[1])
    elif command[0] == "all":
        s = (1 << 21) - 1
    elif command[0] == "empty":
        s = 0 
    