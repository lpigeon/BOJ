import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

case1 = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
case2 = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"
error = []
case1count = 0
case2count = 0
chess = []
schess = []
for _ in range(m):
    chess.append(sys.stdin.readline().rstrip())

m += 1
n += 1

for j in range(n-8):
    for i in range(m-8):
        for x in range(i,i+8):
            schess.append(chess[x][j:j+8])
        schess = "".join(schess)
        for n in range(64):
            if schess[n] != case1[n]:
                case1count += 1
            if schess[n] != case2[n]:
                case2count += 1
        error.append(min(case1count, case2count))
        case1count = 0
        case2count = 0
        schess = []
print(min(error))