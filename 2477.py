# 참외밭

import sys

k = int(sys.stdin.readline().rstrip())

fieldLen = []

for _ in range(6):
    _, l = map(int, sys.stdin.readline().rstrip().split())
    fieldLen.append(l)
wMax = max(fieldLen[0], fieldLen[2], fieldLen[4])
hMax = max(fieldLen[1], fieldLen[3], fieldLen[5])
temp = fieldLen.copy()
wMaxIndex = fieldLen.index(wMax)
temp[wMaxIndex] = 0
hMaxIndex = temp.index(hMax)

if wMaxIndex < hMaxIndex:
    notAreaIndexOfw = wMaxIndex - 2
    if notAreaIndexOfw < 0:
        notAreaIndexOfw += 6
    notAreaIndexOfh = hMaxIndex + 2
    if notAreaIndexOfh > 5:
        notAreaIndexOfh -= 6
else:
    notAreaIndexOfh = hMaxIndex - 2
    if notAreaIndexOfh < 0:
        notAreaIndexOfh += 6
    notAreaIndexOfw = wMaxIndex + 2
    if notAreaIndexOfw > 5:
        notAreaIndexOfw -= 6
wMin = fieldLen[notAreaIndexOfw]
hMin = fieldLen[notAreaIndexOfh]

area = wMax*hMax - wMin*hMin

print(k*area)


