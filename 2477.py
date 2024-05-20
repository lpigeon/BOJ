# 참외밭

import sys

k = int(sys.stdin.readline().rstrip())

field_axis_list = []
x, y = 0, 0

for _ in range(6):
    axis, length = map(int, sys.stdin.readline().rstrip().split())
    
    # axis 1:east, 2:west, 3:south, 4:north
    if axis == 1:
        x += length
        y += 0
    elif axis == 2:
        x -= length
        y += 0
    elif axis == 3:
        x += 0
        y -= length
    elif axis == 4:
        x += 0
        y += length
    field_axis_list.append((x, y))
    
# calculate area
area = 0
for i in range(6):
    area += field_axis_list[i][0] * field_axis_list[(i+1)%6][1] - field_axis_list[i][1] * field_axis_list[(i+1)%6][0]
area = abs(area) / 2

print(int(area * k))