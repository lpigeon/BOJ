import sys
n = int(sys.stdin.readline().rstrip())
vps_stack = []

for _ in range(n):
    s = list(sys.stdin.readline().rstrip())
    for i in s:
        if i == "(":
            vps_stack.append(i)
        elif i == ")":
            if len(vps_stack) == 0:
                vps_stack.append(i)
                break
            vps_stack.pop()
    if len(vps_stack) != 0:
        print("NO")
    elif len(vps_stack) == 0:
        print("YES") 
    vps_stack = []
            